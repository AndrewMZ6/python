from abc import ABC, abstractmethod


class Observer(ABC):

	@abstractmethod
	def update(self):
		"""Reaction to subject notifications"""


class Subject(ABC):

	@abstractmethod
	def attach(self, observer: Observer):
		"""Add new observer to observers list"""

	@abstractmethod
	def detach(self, observer: Observer):
		"""Remove observer to observers list"""

	@abstractmethod
	def notify(self):
		"""Notify every observer in observers list"""


class concrete_Observer_1(Observer):
	def __init__(self, name: str) -> None:
		self.name = name
		
	def update(self) -> None:
		print(f"-> {self.name} sees the notification!")


class Publisher(Subject):
	def __init__(self) -> None:
		self.observer_list: list[Observer] = []
		self._notification_counter = 0

	def attach(self, observer: Observer) -> None:
		if observer not in self.observer_list:
			self.observer_list.append(observer)

	def detach(self, observer: Observer) -> None:
		self.observer_list.remove(observer)

	def notify(self) -> None:

		if self.observer_list:
			self._notification_counter += 1
			print(f'Notification # {self._notification_counter}. {self.__class__.__name__} notifies observers')
			for observer in self.observer_list:
				observer.update()
		else:
			print('The observer list is empty. Nobody\'s interested :(')



if __name__ == '__main__':

	# A group of scientists observes termometer data
	Ivan = concrete_Observer_1('Ivan')
	Masha = concrete_Observer_1('Masha')
	Georgy = concrete_Observer_1('Georgy')

	# A termometer that periodycally sends data
	termometer = Publisher()

	termometer.attach(Ivan)
	termometer.notify()

	termometer.attach(Masha)
	termometer.notify()

	termometer.detach(Masha)
	termometer.notify()

	termometer.attach(Georgy)
	termometer.notify()

	termometer.detach(Ivan)
	termometer.notify()
	termometer.notify()

	termometer.detach(Georgy)
	termometer.notify()
	termometer.notify()


	termometer.attach(Ivan)
	termometer.notify()

	termometer.attach(Masha)
	termometer.notify()


# OUTPUT:
# Notification # 1. Publisher notifies observers
# -> Ivan sees the notification!
# Notification # 2. Publisher notifies observers
# -> Ivan sees the notification!
# -> Masha sees the notification!
# Notification # 3. Publisher notifies observers
# -> Ivan sees the notification!
# Notification # 4. Publisher notifies observers
# -> Ivan sees the notification!
# -> Georgy sees the notification!
# Notification # 5. Publisher notifies observers
# -> Georgy sees the notification!
# Notification # 6. Publisher notifies observers
# -> Georgy sees the notification!
# The observer list is empty. Nobody's interested :(
# The observer list is empty. Nobody's interested :(
# Notification # 7. Publisher notifies observers
# -> Ivan sees the notification!
# Notification # 8. Publisher notifies observers
# -> Ivan sees the notification!
# -> Masha sees the notification!