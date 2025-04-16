from abc import ABC, abstractmethod
import threading
# class CityHall:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             print('Створюємо єдину мерію міста')
#             cls._instance = super().__new__(cls,*args, **kwargs)
#         else:
#             print('Already created')
#
#         return cls._instance
#
#     def serve_citizen(self, citizen_name):
#         print(f'Мерія обслуговує громадянина {citizen_name}')
#
# hall1 = CityHall()
# hall2 = CityHall()
#
# print(hall1 is hall2)

#
# class Toy(ABC):
#     @abstractmethod
#     def play(self):
#         pass
#
# class Ball(Toy):
#     def play(self):
#         print('Play with ball')
#
# class Car(Toy):
#     def play(self):
#         print('Play with car')
#
# class Bear(Toy):
#     def play(self):
#         print('Play with bear')
#
# class ToyFactory(ABC):
#     @abstractmethod
#     def create_toy(self) -> Toy:
#         pass
#
# class BallFactory(ToyFactory):
#     def create_toy(self) -> Toy:
#         return Ball()
#
# class CarFactory(ToyFactory):
#     def create_toy(self) -> Toy:
#         return Car()
#
# class BearFactory(ToyFactory):
#     def create_toy(self) -> Toy:
#         return Bear()
#
# def produce_toy(factory: ToyFactory):
#     toy = factory.create_toy()
#     toy.play()
#
# produce_toy(BallFactory())
# produce_toy(BearFactory())
# produce_toy(CarFactory())


# class SocialMediaAccount:
#     def __init__(self, username):
#         self.username = username
#         self.followers = []
#
#     def subscribe(self, observer):
#         self.followers.append(observer)
#
#     def unsubscribe(self, observer):
#         self.followers.remove(observer)
#
#     def new_post(self, content):
#         print(f'{self.username} опублікував(ла) новий пост: {content}')
#         self.notify_followers(content)
#
#     def notify_followers(self, content):
#         for follower in self.followers:
#             follower.update(self, content)
#
# class Follower:
#     def __init__(self, name):
#         self.name = name
#
#     def update(self, account : SocialMediaAccount, content):
#         print(f'{self.name} отримав(ла) сповіщення: {account.username} - {content}')
#
# account = SocialMediaAccount('Bob')
# follower1 = Follower('Alice')
# follower2 = Follower('Ivan')
#
# account.subscribe(follower1)
# account.subscribe(follower2)
#
# account.new_post('Hello')
#
# account.unsubscribe(follower2)
#
# account.new_post('Hi')

# class ExternalDevice:
#     def plug_in(self):
#         print('Пристрій підключено за допомогою методу plug_in')
#
# class DeviceInterface:
#     def connect(self):
#         raise NotImplementedError
#
# class DeviceAdapter(DeviceInterface):
#     def __init__(self, external_device: ExternalDevice):
#         self.external_device = external_device
#
#     def connect(self):
#         self.external_device.plug_in()
#
# external_device = ExternalDevice()
# adapter = DeviceAdapter(external_device)
# adapter.connect()


# class RouteStrategy(ABC):
#     @abstractmethod
#     def get_route(self, start, end):
#         pass
#
# class FastRoute(RouteStrategy):
#     def get_route(self, start, end):
#         return f'Швидкий маршрут від {start} до {end}'
#
# class ScenicRoute(RouteStrategy):
#     def get_route(self, start, end):
#         return f'Scenic route from {start} to {end}'
#
# class Navigator:
#     def __init__(self, strategy: RouteStrategy):
#         self.strategy = strategy
#
#     def set_strategy(self, strategy: RouteStrategy):
#         self.strategy = strategy
#
#     def navigate(self, start, end):
#         route = self.strategy.get_route()
#         print(route)
#
# navigator = Navigator(FastRoute())
#
# navigator.navigate('City 1', 'City 2')

# class Command(ABC):
#     @abstractmethod
#     def execute(self):
#         pass
#
# class TV:
#     def on(self):
#         print('TV is on')
#     def off(self):
#         print('TV is off')
#
# class TVOnCommand(Command):
#     def __init__(self, tv: TV):
#         self.tv = tv
#
#     def execute(self):
#         self.tv.on()
#
# class TvOffCommand(Command):
#     def __init__(self, tv: TV):
#         self.tv = tv
#
#     def execute(self):
#         self.tv.off()
#
# class RemoteControl:
#     def __init__(self):
#         self.commands = {}
#     def add_command(self, num_btn, command: Command):
#         self.commands[num_btn] = command
#
#     def press_btn(self, num_btn):
#         return self.commands.get(num_btn).execute()
#
# tv = TV()
# remote = RemoteControl()
#
# remote.add_command(1, TVOnCommand(tv))
# remote.add_command(2, TvOffCommand(tv))
# remote.press_btn(1)
# remote.press_btn(2)

# class TrafficLightState(ABC):
#     @abstractmethod
#     def handle(self, traffic_light):
#         pass
#
# class RedState(TrafficLightState):
#     def handle(self, traffic_light):
#         print('Red Light: STOP!')
#         traffic_light.state = YellowState()
#
# class YellowState(TrafficLightState):
#     def handle(self, traffic_light):
#         print('Yelow Light: READY!')
#         traffic_light.state = GreenState()
# class GreenState(TrafficLightState):
#     def handle(self, traffic_light):
#         print('Green State: GO, GO, GO!!!')
#         traffic_light.state = RedState()
#
# class TrafficLight:
#     def __init__(self):
#         self.state: TrafficLightState = RedState()
#
#     def change(self):
#         self.state.handle(self)
#
# light = TrafficLight()
# for _ in range(6):
#     light.change()

# class Kitchen:
#     def __init__(self):
#         self.orders = {}
#
#     def add_order(self, table, order):
#         self.orders[table] = order
#         print(f'Kitchen take order {table} - {order}')
#
#     def get_order(self, table):
#         return self.orders.get(table, 'Order is not found')
#
#
# class DiningRoom:
#     def display_order(self, table, order):
#         print(f'Table {table} get order {order}')
#
# class Waiter:
#     def __init__(self, kitchen: Kitchen, dining_room = DiningRoom):
#         self.kitchen = kitchen
#         self.dining_room = dining_room
#
#     def take_oder(self, table, order):
#         print(f'Waiter: Take order {table}')
#         self.kitchen.add_order(table, order)
#
#     def serve_order(self, table, order):
#         order = self.kitchen.get_order(table)
#         self.dining_room.display_order(table, order)
#
# kitchen = Kitchen()
# dining_room = DiningRoom()
# waiter = Waiter(kitchen, dining_room)
# waiter.take_oder(5, 'pizza')


# class DBConnection:
#     _instance = None
#     _lock = threading.Lock()
#
#     def __new__(cls):
#         with cls._lock:
#             if cls._instance is None:
#                 cls._instance = super().__new__(cls)
#             return cls._instance
#
#     def connect(self):
#         self.connection = 'Connection to DB ready'
#
# db1 = DBConnection()
# db2 = DBConnection()
# print(db1 is db2)

# class Notification(ABC):
#     @abstractmethod
#     def send(self, message):
#         raise NotImplementedError
#
# class EmailNotification(Notification):
#     def send(self, message):
#         print(f'[EMAIL] {message}')
# class SMSNotification(Notification):
#     def send(self, message):
#         print(f'[SMS] {message}')
# class PushNotification(Notification):
#     def send(self, message):
#         print(f'[PUSH] {message}')
# class NotificationFactory:
#     @staticmethod
#     def create_notification(method):
#         if method == 'email':
#             return EmailNotification()
#         elif method == 'sms':
#             return SMSNotification()
#         elif method == 'push':
#             return PushNotification()
# notifier = NotificationFactory.create_notification('sms')
# notifier.send('Hello user')

# class Order:
#     def __init__(self):
#         self._observers = []
#         self.status = 'New'
#
#     def attach(self, observers):
#         self._observers.append(observers)
#
#     def set_status(self, new_status):
#         self.status = new_status
#         self.notify_all()
#
#     def notify_all(self):
#         for obs in self._observers:
#             obs.update(self.status)
# class EmailObserver:
#     def update(self, status):
#         print(f'New order status {status}')
#
# order = Order()
#
# order.attach(EmailObserver())
# order.set_status('Ready')

# class ExternalCurrencyAPI:
#     def get_rate(self):
#         return {'usd': 38.1, 'eur': 41.5}
#
# class CurrencyAdapter:
#     def __init__(self, api):
#         self.api = api
#
#     def get_usd_rate(self):
#         return self.api.get_rate()['usd']
#
# api = ExternalCurrencyAPI()
# adapter = CurrencyAdapter(api)
# print(f'USD: {adapter.get_usd_rate()}')


# class DiscountStrategy:
#     def apply(self, price):
#         pass
#
# class NoDiscount(DiscountStrategy):
#     def apply(self, price):
#         return price
#
# class TenPercentDiscount(DiscountStrategy):
#     def apply(self, price):
#         return price * 0.9
#
# class LoyalCustomerDiscount(DiscountStrategy):
#     def apply(self, price):
#         return price * 0.8
#
# class OrderNavigator:
#     def __init__(self, price, strategy):
#         self.price = price
#         self.strategy = strategy
#
#     def set_strategy(self, strategy):
#         self.strategy = strategy
#
#     def final_price(self):
#         return self.strategy.apply(self.price)
#
# order = OrderNavigator(1000, NoDiscount())
# print(order.final_price())
# order.set_strategy(TenPercentDiscount())
# print(order.final_price())

# class AccountState:
#     def do_action(self):
#         pass
#
# class ActiveState(AccountState):
#     def do_action(self):
#         print('Active user')
#
# class BlockedState(AccountState):
#     def do_action(self):
#         print('Block user')
#
# class Account:
#     def __init__(self):
#         self.state = AccountState()
#     def set_state(self, state):
#         self.state = state
#
#     def action(self):
#         self.state.do_action()
# acc = Account()
# acc.action()
# acc.set_state(BlockedState())
# acc.action()


# class UserModel:
#     def __init__(self, username):
#         self.username = username
#
# class UserController:
#     def create_user(self, username):
#         user = UserModel(username)
#         return UserView.render(user)
#
# class UserView:
#     @staticmethod
#     def render(user):
#         return {'username': user.username, 'status': 'created'}
#
# ctrl = UserController()
# print(ctrl.create_user('user_bob2025'))