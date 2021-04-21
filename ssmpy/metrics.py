from ssmpy.data import *
from ssmpy.calculations import *
import multiprocessing as mp


def get_all_commom_ancestors(all_ancestors, it1, it2):
    """Get all common ancestors for it1 and it2

    :param all_ancestors: pandas DataFrame of all ancestors
    :param it1: entity 1 (id)
    :param it2: entity 2 (id)
    :return: pandas DataDrame of common ancestors or zero

    """

    # get all ancestors for it1 and it2
    all_ancestors_it1_it2 = all_ancestors[(all_ancestors.entry1 == it1) | (all_ancestors.entry1 == it2)]

    # common_ancestors = all_ancestors_it1_it2['entry2'].value_counts().reset_index(name="count").query("count > 1")[
    #    'index'].to_list()

    # get the common ancestors for it1 and it2
    common_ancestors = all_ancestors_it1_it2.groupby('entry2')['entry1'].apply(
        lambda x: x.unique()).reset_index()
    common_ancestors = common_ancestors[common_ancestors['entry1'].str.len() > 1].entry2.to_list()

    if len(common_ancestors) > 0:
        return common_ancestors

    else:
        return 0


def fast_resnik(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2):
    """Calculates the RESNIK MICA INTRINSIC similarity between it1 and it2
    
    :param all_ancestors: pandas DataFrame of all ancestors (from table transitive)
    :param df_entry_ancestors: pandas DataFrame of all ancestors (from table entry) with column IC
    :param df_entry_ic: pandas DataFrame of all entities (from table entry) with column IC
    :param it1: entity 1 (id)
    :param it2: entity 2 (id)
    :return: list: [e1, e2, sim_resnik]
    """

    if it1 == it2:

        sim_resnik = df_entry_ic[df_entry_ic.id == it1].IC.to_list()[0]

    else:
        common_ancestors = get_all_commom_ancestors(all_ancestors, it1, it2)

        if common_ancestors == 0:

            sim_resnik = 0

        else:

            # get max ic for the common ancestors (MICA)
            ic_ancestors = df_entry_ancestors[df_entry_ancestors.id.isin(common_ancestors)].IC

            sim_resnik = ic_ancestors.max()

    print((df_entry_ic[df_entry_ic.id == it1].name.to_list()[0]),
          (df_entry_ic[df_entry_ic.id == it2].name.to_list()[0]), " RESNIK:MICA:INTRINSIC ",
          sim_resnik)

    return [df_entry_ic[df_entry_ic.id == it1].name.to_list()[0], df_entry_ic[df_entry_ic.id == it2].name.to_list()[0],
            sim_resnik]


def fast_lin(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2):
    """Calculates the LIN MICA INTRINSIC similarity between it1 and it2

    :param all_ancestors: pandas DataFrame of all ancestors (from table transitive)
    :param df_entry_ancestors: pandas DataFrame of all ancestors (from table entry) with column IC
    :param df_entry_ic: pandas DataFrame of all entities (from table entry) with column IC
    :param it1: entity 1 (id)
    :param it2: entity 2 (id)
    :return: list: [e1, e2, sim_lin]
    """

    if it1 == it2:
        sim_lin = 1

    else:

        common_ancestors = get_all_commom_ancestors(all_ancestors, it1, it2)

        if common_ancestors == 0:
            sim_lin = 0

        else:

            # get max ic for the common ancestors (MICA)
            ic_ancestors_max = df_entry_ancestors[df_entry_ancestors.id.isin(common_ancestors)].IC.max()

            sim_lin = (2 * ic_ancestors_max) / (
                    df_entry_ic[df_entry_ic.id == it1].IC.to_list()[0] +
                    df_entry_ic[df_entry_ic.id == it2].IC.to_list()[0])

    # print((df[df.id == it1].name.to_list()[0]), (df[df.id == it2].name.to_list()[0]), " LIN:MICA:INTRINSIC ",
    #      sim_lin)

    return [df_entry_ic[df_entry_ic.id == it1].name.to_list()[0], df_entry_ic[df_entry_ic.id == it2].name.to_list()[0],
            sim_lin]


def fast_jc(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2):
    """Calculates the JC MICA INTRINSIC similarity between it1 and it2

    :param all_ancestors: pandas DataFrame of all ancestors (from table transitive)
    :param df_entry_ancestors: pandas DataFrame of all ancestors (from table entry) with column IC
    :param df_entry_ic: pandas DataFrame of all entities (from table entry) with column IC
    :param it1: entity 1 (id)
    :param it2: entity 2 (id)
    :return: list: [e1, e2, sim_jc]
    """

    if it1 == it2:

        sim_jc = 1

    else:

        common_ancestors = get_all_commom_ancestors(all_ancestors, it1, it2)

        if common_ancestors == 0:

            ic_ancestors_max = 0

        else:

            # get max ic for the common ancestors (MICA)
            ic_ancestors_max = df_entry_ancestors[df_entry_ancestors.id.isin(common_ancestors)].IC.max()

        distance = df_entry_ic[df_entry_ic.id == it1].IC.to_list()[0] + df_entry_ic[df_entry_ic.id == it2].IC.to_list()[
            0] - (
                           2 * ic_ancestors_max)

        if distance > 0:
            sim_jc = 1 / (distance + 1)
        else:
            sim_jc = 1

    print((df_entry_ic[df_entry_ic.id == it1].name.to_list()[0]),
          (df_entry_ic[df_entry_ic.id == it2].name.to_list()[0]), " JC:MICA:INTRINSIC ",
          sim_jc)

    return [df_entry_ic[df_entry_ic.id == it1].name.to_list()[0], df_entry_ic[df_entry_ic.id == it2].name.to_list()[0],
            sim_jc]


def fast_resn_lin_jc(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2):
    """ Calculates the RESNIK, LIN and JC MICA INTRINSIC similarity between it1 and it2

    :param all_ancestors: pandas DataFrame of all ancestors (from table transitive)
    :param df_entry_ancestors: pandas DataFrame of all ancestors (from table entry) with column IC
    :param df_entry_ic: pandas DataFrame of all entities (from table entry) with column IC
    :param it1: entity 1 (id)
    :param it2: entity 2 (id)
    :return: list: [e1, e2, sim_resnik, sim_lin, sim_jc]
    """

    if it1 == it2:

        sim_resnik = df_entry_ic[df_entry_ic.id == it1].IC.to_list()[0]
        sim_lin = 1
        sim_jc = 1

    else:
        common_ancestors = get_all_commom_ancestors(all_ancestors, it1, it2)

        if common_ancestors == 0:

            sim_resnik = 0
            sim_lin = 0
            ic_ancestors_max_jc = 0


        else:

            # get max ic for the common ancestors (MICA)
            ic_ancestors_resn = df_entry_ancestors[df_entry_ancestors.id.isin(common_ancestors)].IC

            sim_resnik = ic_ancestors_resn.max()

            ic_ancestors_max_lin = df_entry_ancestors[df_entry_ancestors.id.isin(common_ancestors)].IC.max()
            ic_ancestors_max_jc = df_entry_ancestors[df_entry_ancestors.id.isin(common_ancestors)].IC.max()

            sim_lin = (2 * ic_ancestors_max_lin) / (
                    df_entry_ic[df_entry_ic.id == it1].IC.to_list()[0] +
                    df_entry_ic[df_entry_ic.id == it2].IC.to_list()[0])

        distance = df_entry_ic[df_entry_ic.id == it1].IC.to_list()[0] + df_entry_ic[df_entry_ic.id == it2].IC.to_list()[
            0] - (
                           2 * ic_ancestors_max_jc)

        if distance > 0:
            sim_jc = 1 / (distance + 1)
        else:
            sim_jc = 1

    return [df_entry_ic[df_entry_ic.id == it1].name.to_list()[0], df_entry_ic[df_entry_ic.id == it2].name.to_list()[0],
            sim_resnik, sim_lin, sim_jc]


# def light_similarity(conn, entry_ids_1, entry_ids_2, metric):
#     """
#     main function
#     :param conn: db_connection
#     :param entry_ids_1: list of entries 1
#     :param entry_ids_2: list of entries 2
#     :param metric: 'lin', 'resnick', 'jc' or 'all'
#     :return: list with results ([e1, e2, similarity] or [e1, e2, similarity resnik, similarity lin, similarity jc])
#     """
#
#     results = []
#
#     # concatenate both list of entries
#     entry_ids = np.unique(np.array(entry_ids_1 + entry_ids_2)).tolist()
#
#     df_entry = db_select_entry(conn, entry_ids)
#
#     # ids for each name in both lists
#     ids_list = df_entry.id.values.flatten()
#
#     # ids for each list
#     ids_list_1 = df_entry[df_entry.name.isin(entry_ids_1)].id.values.flatten()
#     ids_list_2 = df_entry[df_entry.name.isin(entry_ids_2)].id.values.flatten()
#
#     if np.array_equal(ids_list_1, ids_list_2):
#
#         # get all the ancestors for test_ids in transitive table
#         all_ancestors = db_select_transitive(conn, ids_list)
#
#         # get all ancestors in entry table
#         df_entry_ancestors = db_select_entry_by_id(conn, all_ancestors.entry2.values.flatten())
#
#         # get max freq used for calculating the Information Content (IC)
#         max_freq = get_max_dest(conn)
#
#         # calculates Ic for original IDs
#         df_entry_ic = calculate_information_content_intrinsic(df_entry, max_freq)
#
#         # calculates IC for all ancestors
#         df_entry_ancestors = calculate_information_content_intrinsic(df_entry_ancestors, max_freq)
#
#         if metric == 'resnik':
#
#             for it1 in ids_list_1:
#                 pool = mp.Pool(20)
#                 results.append(pool.starmap(fast_resnik,
#                                             [(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2) for it2 in
#                                              ids_list_1]))
#
#                 pool.close()
#
#                 mask = np.where(ids_list_1 == it1)
#                 ids_list_1 = np.delete(ids_list_1, mask)
#
#         elif metric == 'lin':
#             count = 0
#             for it1 in ids_list_1:
#                 print(count, ..., len(ids_list_1))
#                 count += 1
#
#                 pool = mp.Pool(20)
#                 results.append(pool.starmap(fast_lin,
#                                             [(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2) for it2 in
#                                              ids_list_1]))
#
#                 pool.close()
#
#                 mask = np.where(ids_list_1 == it1)
#                 ids_list_1 = np.delete(ids_list_1, mask)
#
#         elif metric == 'jc':
#
#             for it1 in ids_list_1:
#                 pool = mp.Pool(20)
#                 results.append(pool.starmap(fast_jc,
#                                             [(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2) for it2 in
#                                              ids_list_1]))
#
#                 pool.close()
#
#                 mask = np.where(ids_list_1 == it1)
#                 ids_list_1 = np.delete(ids_list_1, mask)
#
#
#         elif metric == 'all':
#
#             for it1 in ids_list_1:
#                 pool = mp.Pool(20)
#
#                 results.append(pool.starmap(fast_resn_lin_jc,
#                                             [(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2) for it2 in
#                                              ids_list_1]))
#
#                 pool.close()
#                 mask = np.where(ids_list_1 == it1)
#                 ids_list_1 = np.delete(ids_list_1, mask)
#
#     else:
#
#         # get all the ancestors for test_ids in transitive table
#         all_ancestors = db_select_transitive(conn, ids_list)
#
#         # get all ancestors in entry table
#         df_entry_ancestors = db_select_entry_by_id(conn, all_ancestors.entry2.values.flatten())
#
#         # get max freq used for calculating the Information Content (IC)
#         max_freq = get_max_dest(conn)
#
#         # calculates Ic for original IDs
#         df_entry_ic = calculate_information_content_intrinsic(df_entry, max_freq)
#
#         # calculates IC for all ancestors
#         df_entry_ancestors = calculate_information_content_intrinsic(df_entry_ancestors, max_freq)
#
#         if metric == 'resnik':
#
#             for it1 in ids_list_1:
#                 pool = mp.Pool(20)
#                 results.append(pool.starmap(fast_resnik,
#                                             [(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2) for it2 in
#                                              ids_list_2]))
#
#                 pool.close()
#
#                 mask = np.where(ids_list_1 == it1)
#                 ids_list_1 = np.delete(ids_list_1, mask)
#
#         elif metric == 'lin':
#             count = 0
#             for it1 in ids_list_1:
#                 print(count, ..., len(ids_list_1))
#                 count += 1
#
#                 pool = mp.Pool(20)
#                 results.append(pool.starmap(fast_lin,
#                                             [(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2) for it2 in
#                                              ids_list_2]))
#
#                 pool.close()
#
#                 mask = np.where(ids_list_1 == it1)
#                 ids_list_1 = np.delete(ids_list_1, mask)
#
#         elif metric == 'jc':
#
#             for it1 in ids_list_1:
#                 pool = mp.Pool(20)
#                 results.append(pool.starmap(fast_jc,
#                                             [(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2) for it2 in
#                                              ids_list_2]))
#
#                 pool.close()
#
#                 mask = np.where(ids_list_1 == it1)
#                 ids_list_1 = np.delete(ids_list_1, mask)
#
#
#         elif metric == 'all':
#
#             for it1 in ids_list_1:
#                 pool = mp.Pool(20)
#
#                 results.append(pool.starmap(fast_resn_lin_jc,
#                                             [(all_ancestors, df_entry_ancestors, df_entry_ic, it1, it2) for it2 in
#                                              ids_list_2]))
#
#                 pool.close()
#                 mask = np.where(ids_list_1 == it1)
#                 ids_list_1 = np.delete(ids_list_1, mask)
#
#     return results
