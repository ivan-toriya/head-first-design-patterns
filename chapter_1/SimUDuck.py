class FlyBehavior:
    def fly(self):
        raise NotImplementedError


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly!")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


class QuackBehavior:
    def quack(self):
        raise NotImplementedError


class Quack(QuackBehavior):
    def quack(self):
        print("Quack, quack, quack!")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak, squeak, squeak!")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Duck:
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def set_fly_behavior(self, fb: FlyBehavior):
        self.fly_behavior = fb

    def set_quack_behavior(self, qb: QuackBehavior):
        self.quack_behavior = qb

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def swim(self):
        print("All ducks float, even decoys!")

    def display(self):
        raise NotImplementedError


class MallardDuck(Duck):
    def __init__(self):
        super().__init__(fly_behavior=FlyWithWings(), quack_behavior=Quack())

    def display(self):
        print("I'm a real Mallard duck.")


class ModelDuck(Duck):
    def __init__(self):
        super().__init__(fly_behavior=FlyNoWay(), quack_behavior=Quack())

    def display(self):
        print("I'm a model duck.")


mallard = MallardDuck()
mallard.perform_quack()
mallard.perform_fly()

print("------")

model = ModelDuck()
model.perform_fly()
model.set_fly_behavior(FlyRocketPowered())
model.perform_fly()
