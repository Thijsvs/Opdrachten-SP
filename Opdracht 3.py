import psycopg2
import random
import ast


def data_collection():
    # info over visitor
    cur.execute("select profile_id, buids, viewed_before, similars, previously_recommended from profiles where viewed_before is not null" )
    visitor_data = cur.fetchall()

    # info over product
    cur.execute('select product_id, category, sub_category, sub_sub_category, doelgroep, gender, herhaalaankopen, discount from products ')
    product_data = cur.fetchall()

    # info over session
    cur.execute('select buid from sessions')
    session_data = cur.fetchall

    return visitor_data, product_data, session_data

def profile_comparisment(objective, table, column, input):
    cur.execute("select %s from %s where %s like '%s'" % (objective, table, column, '%' + input + '%'))
    recommendation = cur.fetchall()
    return recommendation


def collaborive():
    # random profile
    randompf = random.randint(0, len(visitor_info) - 1)
    pfID = visitor_info[randompf][0]
    # viewed before list maken
    viewed_before = visitor_info[randompf][2]
    viewed_before = viewed_before.strip('}{').split(',')
    lst_viewedbefore = list(viewed_before)


    suggestions = []

    for x in lst_viewedbefore:
        results = profile_comparisment('previously_recommended', 'profiles', 'viewed_before', x)
        suggestions.append(results)
    recommended = []
    for x in suggestions:
        for lst in x:
            if lst[0] == None:
                coninue
            else:
                lst = list(lst[0].strip('{}').split(','))
                for value in lst:
                    if value in suggestions:
                        continue
                    else:
                        recommended.append(value)

    cur.execute('drop table if exists collaborative_filtering')
    cur.execute('create table collaborative_filtering(profile_id VARCHAR(30) NOT NULL, recom_productID VARCHAR(10000000) NOT NULL, FOREIGN KEY(profile_id) REFERENCES profiles(profile_id))')
    cur.execute('insert into collaborative_filtering(profile_id, recom_productID) values (%s, %s)', (pfID, suggestions))
    return




def content():
    # random profile
    randompf = random.randint(0, len(visitor_info) - 1)
    pfID = visitor_info[randompf][0]
    # viewed before list maken
    viewed_before = visitor_info[randompf][2]
    viewed_before = viewed_before.strip('}{').split(',')
    lst_viewedbefore = list(viewed_before)


    recommendation = []
    results = profile_comparisment('viewed_before', 'profiles', 'profile_id', pfID )
    recommendation.append(results)

    cur.execute('drop table if exists content_filtering')
    cur.execute( 'create table content_filtering(profile_id VARCHAR(30) NOT NULL, recom_productID VARCHAR(10000000) NOT NULL, FOREIGN KEY(profile_id) REFERENCES profiles(profile_id))')
    cur.execute('insert into content_filtering(profile_id, recom_productID) values (%s, %s)', (pfID, recommendation))

    return

def product_comparisment():
    cur.execute("select %s from %s where %s like '%s'" % (objective, table, column, '%' + input + '%'))
    recommendation = cur.fetchall()
    return recommendation

con = psycopg2.connect(
    host="localhost",
    database="HuWebshop",
    user="Thijs van Spingelen",
    password="thijs"
)
cur = con.cursor()


visitor_info, product_info, session_info = data_collection()
# collaborive()
content()
con.commit()
cur.close()
con.close()