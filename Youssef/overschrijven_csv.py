import pymongo
import csv

'''Verbinden van pymongo en psycopg2 met python'''
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["huwebshop"]
print(myclient.list_database_names())

def schrijven():
    print("Creating the product database contents...")

    def inhoud_producten():
        '''geselecteerde inhoud van producten opvragen'''
        with open('products.csv', 'w', newline='') as csvout:
            fieldnames = ['id', 'brand', 'category', 'subcategory', 'subsubcategory', 'color', 'gender',
                          'herhaalaankopen', 'name', 'price.selling_price', 'recommendable']
            writer = csv.DictWriter(csvout, fieldnames=fieldnames)
            writer.writeheader()
            c = 0
            for product in mydb.products.find():
                try:
                    if product['price']['selling_price'] != 0:
                        writer.writerow({'id': product["_id"],
                                         'brand': product.get('brand', None),
                                         'category': product.get("category", None),
                                         'subcategory': product.get("sub_category", None),
                                         'subsubcategory': product.get("sub_sub_category", None),
                                         'color': product.get("color", None),
                                         'gender': product.get('gender', None),
                                         'herhaalaankopen': product.get('herhaalaankopen', None),
                                         'name': product.get('name', None),
                                         'price.selling_price': product.get("price", {"selling_price": None})[
                                             "selling_price"],
                                         'recommendable': product.get('recommendable', None)
                                         })
                except:
                    continue
                c += 1
                if c % 10000 == 0:
                    print("{} product records written...".format(c))

    def inhoud_profiles():
        '''geselecteerde inhoud van profielen opvragen'''
        with open('profiles.csv', 'w', newline='') as csvout:
            fieldnames = ['id', ]
            writer = csv.DictWriter(csvout, fieldnames=fieldnames)
            writer.writeheader()
            c = 0
            for profiles in mydb.profiles.find():
                try:
                    writer.writerow({'id': profiles["_id"]})
                except:
                    continue
                c += 1
                if c % 10000 == 0:
                    print("{} product records written...".format(c))

    def inhoud_sessions():
        '''geselecteerde inhoud van sessies opvragen'''
        with open('sessions.csv', 'w', newline='') as csvout:
            fieldnames = ['id', 'session_start', 'session_end',
                          'has_sale', 'order', 'segment', 'preferences.category',
                          'preferences.sub_category', 'preferences.sub_sub_category']
            writer = csv.DictWriter(csvout, fieldnames=fieldnames)
            writer.writeheader()
            c = 0
            for sessions in mydb.sessions.find():
                try:
                    writer.writerow({'id': sessions["_id"],
                                     'session_start': sessions.get('session_start', None),
                                     'session_end': sessions.get('session_end', None),
                                     'has_sale': sessions.get('has_sale', None),
                                     'order': sessions.get('order', None),
                                     'segment': sessions.get('segment', None),

                                     # 'preferences.category': sessions.get('x', None),
                                     # 'preferences.sub_category': sessions.get('x', None),
                                     # 'preferences.sub_sub_category': sessions.get('x', None),
                                     })
                except:
                    continue
                c += 1
                if c % 10000 == 0:
                    print("{} product records written...".format(c))

    # inhoud_producten()
    # inhoud_profiles()
    inhoud_sessions()
    print("Finished creating the product database contents.")
schrijven()