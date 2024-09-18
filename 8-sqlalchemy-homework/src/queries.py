from database import Base, engine, session_factory
from models import Clients, Suppliers, Supplies, Goods, Employees, Orders

from sqlalchemy import Integer, Numeric, cast, func, text, select
from sqlalchemy.orm import aliased


class InsertQuery:
    """Класс, отвечающий за вставку данных в БД."""
    @staticmethod
    def create_tables():
        Base.metadata.drop_all(engine)
        Base.metadata.create_all(engine)

    @staticmethod
    def insert_clients() -> None:
        """Добавляет 10 записей в таблицу clients"""
        with session_factory() as session:
            dataset = (
                ('Карпова Нина Кирилловна', 'Россия, г. Ульяновск, Железнодорожная ул., д. 2 кв.32', '79708184567'),
                ('Лебедев Владимир Алексеевич', 'Россия, г. Смоленск, Советский пер., д. 13 кв.76', '77195888784'),
                ('Баранов Лев Ильич', 'Россия, г. Смоленск, Советский пер., д. 13 кв.76', '75781741548'),
                ('Губанов Матвей Германович', 'Россия, г. Евпатория, Дружбы ул., д. 16 кв.158', '7661347166'),
                ('Симонова Ольга Ивановна', 'Россия, г. Ульяновск, Приозерная ул., д. 16 кв.105', '7250274622'),
                ('Дмитриев Артём Андреевич', 'Россия, г. Ижевск, Озерная ул., д. 14 кв.193', '72314713079'),
                ('Смирнов Илья Васильевич', 'Россия, г. Калининград, Красноармейская ул., д. 23 кв.42', '783258250840'),
                ('Кондратьев Владимир Семёнович', 'Россия, г. Санкт-Петербург, Луговая ул., д. 14 кв.30', '7153726143'),
                ('Попова Камилла Максимовна', 'Россия, г. Таганрог, Озерная ул., д. 1 кв.117', '71492981207'),
                ('Романова Алиса Марковна', 'Россия, г. Волгодонск, Почтовая ул., д. 18 кв.51', '799207188762')
            )
            clients = [Clients(full_name=data[0], address=data[1], phone=data[2]) for data in dataset]
            session.add_all(clients)
            session.commit()

    @staticmethod
    def insert_suppliers() -> None:
        """Добавляет 10 записей в таблицу suppliers"""

        with session_factory() as session:
            dataset = (
                ('Macron', 'Фокина Алина Олеговна', 'VK', '75299110108', 'Россия, г. Барнаул, Красноармейская ул., д. 23 кв.120'),
                ('DeliveryGood', 'Вавилов Алексей Иванович', 'TG', '734092589901', 'Россия, г. Москва, Почтовая ул., д. 8 кв.130'),
                ('GoodFox', 'Басов Глеб Владиславович', 'OK', '7904149449', 'Россия, г. Тула, Полевая ул., д. 24 кв.142'),
                ('AirProduct', 'Маркова Ариана Демидовна', 'Facebook', '75141245754', 'Россия, г. Грозный, Чапаева ул., д. 19 кв.75'),
                ('MaxQuality', 'Дмитриева Анна Захаровна', 'Twitter', '780676916910', 'Россия, г. Чебоксары, Вишневая ул., д. 4 кв.19'),
                ('ADV', 'Фомин Родион Михайлович', 'VK', '7690906043', 'Россия, г. Елец, Заречный пер., д. 13 кв.38'),
                ('Minsk', 'Высоцкая Кристина Алиевна', 'TG', '7774221128', 'Россия, г. Керчь, Северная ул., д. 9 кв.153'),
                ('GG', 'Вдовин Адам Артёмович', 'Twitter', '724848510216', 'Россия, г. Королёв, Почтовая ул., д. 19 кв.102'),
                ('ALI', 'Голубева Таисия Максимовна', 'VK', '7060022700', 'Россия, г. Благовещенск, Сосновая ул., д. 23 кв.111'),
                ('Nikson', 'Кузнецова Яна Викторовна', 'TG', '7324523861','Россия, г. Чебоксары, Партизанская ул., д. 2 кв.219'),
            )
            suppliers = [Suppliers(name=d[0], representative=d[1], contact=d[2], phone=d[3], address=d[4]) for d in dataset]
            session.add_all(suppliers)
            session.commit()

    @staticmethod
    def insert_supplies() -> None:
        """Добавляет 10 записей в таблицу supplies"""
        with session_factory() as session:
            stmt = text("""INSERT INTO supplies (supplier_id, supply_date) VALUES 
                            (1, '2024-01-02'), (1, '2024-01-10'), (2, '2024-01-24'), 
                            (3, '2024-02-03'), (4, '2024-02-16'), (4, '2024-03-07'),
                            (4, '2024-03-24'), (5, '2024-04-09'), (8, '2024-04-13'),
                            (10, '2024-05-13');"""
            )
            session.execute(stmt)
            session.commit()

    @staticmethod
    def insert_goods() -> None:
        """Добавляет 10 записей в таблицу goods"""
        with session_factory() as session:
            dataset = (
                ('Огурцы', 10, 15, True, 10),
                ('Помидоры', 15, 25, True, 30),
                ('Вафли', 40, 60, True, 40),
                ('Конфеты', 25, 32, False, 0),
                ('Бананы', 20, 27, False, 0),
                ('Шоколад', 30, 40, True, 10),
                ('Курица', 100, 140, True, 3),
                ('Лимонад', 31, 38, True, 10),
                ('Мясо куриное', 120, 180, True, 5),
                ('Яйца', 100, 130, True, 8),
            )

            # получаем всех Supplies
            query = select(Supplies)
            result = session.execute(query)
            supplies = result.scalars().all()

            # добавляем новые записи в таблицу Goods
            goods = []
            for i in range(10):
                good = Goods(name=dataset[i][0],
                             purchase_cost=dataset[i][1],
                             selling_cost=dataset[i][2],
                             is_in_stock=dataset[i][3],
                             count=dataset[i][4])
                print(good.supply)
                good.supply = supplies[i]   # для примера, можно было проще сделать
                goods.append(good)
            session.add_all(goods)
            session.commit()


    @staticmethod
    def insert_employees() -> None:
        """Добавляет 10 записей в таблицу employees"""
        with session_factory() as session:
            dataset = (
                ('Сазонов', 'Марк', 'Владиславович', 'Продавец', '1970-08-02'),
                ('Миронов', 'Матвей', 'Даниилович', 'Грузчик', '1992-03-12'),
                ('Осипова', 'Виктория', 'Давидовна', 'Бухгалтер', '1984-04-01'),
                ('Третьяков', 'Максим', 'Антонович', 'Продавец', '2000-03-03'),
                ('Кириллова', 'Кира', 'Михайловна', 'Грузчик', '2001-04-17'),
                ('Щербаков', 'Богдан', 'Владиславович', 'Уборщик', '1978-12-24'),
                ('Алексеев', 'Александр', 'Максимович', 'Уборщик', '1983-01-05'),
                ('Шестакова', 'Виктория', 'Романовна', 'Владелец', '1969-04-10'),
                ('Кузнецова', 'Алиса', 'Андреевна', 'Продавец', '2002-10-27'),
                ('Павлова', 'София', 'Ярославовна', 'Грузчик', '2001-10-26'),
            )
            employees = []
            for data in dataset:
                employee = Employees(last_name=data[0], first_name=data[1],
                                     middle_name=data[2], position=data[3],
                                     birthday=data[4])
                employees.append(employee)
            session.add_all(employees)
            session.commit()

    @staticmethod
    def insert_orders() -> None:
        """Добавляет 10 записей в таблицу orders"""
        with session_factory() as session:
            stmt = """INSERT INTO orders (employee_id, good_id, posting_date, execution_date, client_id) 
                        VALUES 
                        (1, 1, '2024-05-01', '2024-05-02', 1),
                        (1, 2, '2024-05-01', '2024-05-04', 1),
                        (4, 3, '2024-05-01', '2024-05-09', 4),
                        (9, 4, '2024-05-01', '2024-05-12', 5),
                        (1, 5, '2024-05-04', '2024-05-13', 3),
                        (4, 6, '2024-05-05', '2024-05-14', 2),
                        (4, 1, '2024-05-09', '2024-05-16', 5),
                        (9, 1, '2024-05-10', '2024-05-14', 4),
                        (9, 8, '2024-05-15', '2024-05-21', 9),
                        (4, 2, '2024-05-16', '2024-05-24', 10);"""
            session.execute(text(stmt))
            session.commit()

    @staticmethod
    def insert_all_data():
        """
        Вставляет по 10 записей в каждую из таблиц:
        - clients
        - suppliers
        - supplies
        - goods
        - employees
        - orders
        """
        InsertQuery.insert_clients()
        InsertQuery.insert_suppliers()
        InsertQuery.insert_supplies()
        InsertQuery.insert_goods()
        InsertQuery.insert_employees()
        InsertQuery.insert_orders()


class SelectQuery:
    """Класс, отвечающий за получение данных в БД."""
    @staticmethod
    def get_all_clients():
        """Печатает все записи из таблицы clients."""
        with session_factory() as session:
            query = select(Clients)
            result = session.execute(query)
            clients = result.scalars().all()
            print(f'{clients=}')
            return clients

    @staticmethod
    def get_all_orders_with_relationship_entities() -> None:
        """Соединяет (INNER JOIN) таблицу orders с таблицами clients и employees и выводит все строки."""
        with session_factory() as session:
            query = (
                select(Orders, Clients, Employees)
                .select_from(Orders)
                .join(Clients)
                .join(Employees)
            )
            result = session.execute(query)
            rows = result.all()
            for row in rows:
                print(row)
            return rows

    @staticmethod
    def get_employees_amount_sums() -> None:
        """
        Выводит сотрудника и сумму, на которую он продал товары (цена которых > 20).
        При этом строки сортирует по сумме продаж по убыванию.

        Запрос на языке SQL:
            SELECT DISTINCT employee_id, SUM(selling_cost)::int AS sales_amount FROM orders o
            JOIN goods g ON o.good_id = g.id
            WHERE selling_cost > 20
            GROUP BY employee_id
            ORDER BY sales_amount DESC
        """
        with session_factory() as session:
            o = aliased(Orders)
            g = aliased(Goods)
            query = (
                select(
                    o.employee_id,
                    cast(func.sum(g.selling_cost), Integer).label('sales_amount')
                )
                # .select_from(o)
                .join(g, o.good_id == g.id)  # или просто .join(g)
                .filter(g.selling_cost > 20)
                .group_by(o.employee_id)
                .order_by(func.sum(g.selling_cost).desc())
                # .distinct()     .group_by(o.employee_id) уже гарантирует уникальность
            )
            result = session.execute(query)
            employees_amount_sums = result.all()
            print(f'{employees_amount_sums=}')
            return employees_amount_sums

    @staticmethod
    def get_aggregated_selling_cost_values():
        """
        Группирует записи в таблице goods по наличию на складе
        и выводит агрегирующие функции для цены в каждой группе.

        Запрос на языке SQL:
            SELECT
                is_in_stock,
                COUNT(*),
                AVG(selling_cost)::numeric(10, 2),
                SUM(selling_cost)::numeric(10, 2),
                MIN(selling_cost)::numeric(10, 2),
                MAX(selling_cost)::numeric(10, 2)
            FROM goods
            GROUP BY is_in_stock
        """
        with session_factory() as session:
            query = (
                select(
                    Goods.is_in_stock,
                    func.count(),                   # COUNT(*)
                    cast(func.avg(Goods.selling_cost), Numeric(10, 2)),
                    cast(func.sum(Goods.selling_cost), Numeric(10, 2)),
                    cast(func.min(Goods.selling_cost), Numeric(10, 2)),
                    cast(func.max(Goods.selling_cost), Numeric(10, 2)),
                )                                  # .select_from(Goods)
                .group_by(Goods.is_in_stock)
            )
            result = session.execute(query)
            aggregated_selling_cost_values = result.all()
            print(f'{aggregated_selling_cost_values=}')

            # Более красивый вывод
            for row in aggregated_selling_cost_values:
                is_in_stock = 'В наличии' if row[0] else 'Нет в наличии'
                count, avg, sum_, min_, max_ = [row[1]] + [float(i) for i in row[2:]]
                print(f'{is_in_stock}', f'{count=}', f'{avg=}', f'{sum_=}', f'{min_=}', f'{max_=}', sep='\n\t')
                print()

            return aggregated_selling_cost_values


class UpdateQuery:
    """Класс, отвечающий за изменение данных в БД."""
    @staticmethod
    def update_client_name(client_id: int, new_full_name: str) -> None:
        """Изменяет имя клиента"""
        with session_factory() as session:
            client = session.get(Clients, client_id)
            print(f'Старое имя клиента №{client_id} = {client.full_name}')
            client.full_name = new_full_name
            print(f'Новое имя клиента №{client_id} = {client.full_name}')
            session.commit()


class DeleteQuery:
    """Класс, отвечающий за удаление данных в таблицах БД."""
    @staticmethod
    def delete_first_n_suppliers_with_sql_expression(n: int) -> None:
        """
        Удаляет первые n строк из таблицы с помощью сырого запроса.

        :param n: число первых строк, которые необходимо удалить
        :type n: int

        :return: None
        :type: None
        """
        with session_factory() as session:
            stmt = text("""WITH rows_to_delete AS (
                              SELECT * FROM Suppliers
                              ORDER BY id
                              LIMIT :n
                           )
                           DELETE FROM suppliers
                           USING rows_to_delete
                           WHERE suppliers.id = rows_to_delete.id
            """).bindparams(n=n)
            session.execute(stmt)
            session.commit()

    @staticmethod
    def delete_first_n_suppliers_with_orm(n: int) -> None:
        """
        Удаляет первые n строк из таблицы с помощью ORM-запроса.

        :param n: число первых строк, которые необходимо удалить
        :type n: int

        :return: None
        :type: None
        """
        with session_factory() as session:
            query = (
                select(Suppliers)
                .order_by(Suppliers.id)
                .limit(n)
            )
            suppliers_to_delete = session.execute(query).scalars().all()
            for supplier in suppliers_to_delete:
                session.delete(supplier)
            session.commit()