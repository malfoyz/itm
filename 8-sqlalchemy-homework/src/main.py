from queries import DeleteQuery, InsertQuery, SelectQuery, UpdateQuery



def main():
    InsertQuery.create_tables()
    InsertQuery.insert_all_data()

    SelectQuery.get_all_clients()
    SelectQuery.get_all_orders_with_relationship_entities()

    UpdateQuery.update_client_name(1, 'Иванов Иван Иванович')
    SelectQuery.get_employees_amount_sums()
    SelectQuery.get_aggregated_selling_cost_values()

    # DeleteQuery.delete_first_n_suppliers_with_sql_expression(2)
    DeleteQuery.delete_first_n_suppliers_with_orm(2)


if __name__ == '__main__':
    main()
