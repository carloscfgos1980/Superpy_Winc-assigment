# prints argsparse
'''
    print(items_details(args.item))
    print(items_details(args.yesterday).inventory_yesterday())
    print(items_details(args.today).inventory_today())
    print(items_details(args.storage).in_storage())
    print(items_details(args.revenue_before_yesterday).revenue('before_yesterday'))
    print(items_details(args.revenue_yesterday).revenue('yesterday'))
    print(items_details(args.revenue_today).revenue())
    print(items_details(args.fresh_product).fresh_item())
'''

# trying to print csv
'''
    dic_storage = {
        'item': items_list,
        'initial amount': initial_amount_list,
        'sold': total_sold,
        'in storage': in_storage_list
    }
    df = pd.DataFrame(
        data=dic_storage, columns=[
            'item', 'initial amount', 'sold', 'in storage'])
'''
