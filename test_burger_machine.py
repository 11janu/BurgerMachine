import pytest
# make sure there's an __init__.py in this tests folder and that
# the tests folder is in the same folder as the IcecreamMachine stuff
from BurgerMachine import BurgerMachine
from BurgerMachineExceptions import ExceededRemainingChoicesException, InvalidChoiceException, InvalidStageException, OutOfStockException
#this is an example test showing how to cascade fixtures to build up state

@pytest.fixture
def machine():
    bm = BurgerMachine()
    return bm

@pytest.fixture
def machine1():
    bn = BurgerMachine()
    return bn


def test_bun_must_be_First (machine):
 # UCID is js2679 and date is  23/03/2023
    with pytest.raises (InvalidStageException): 
        machine.handle_patty("veggie") 
        machine.handle_patty("next") 
        machine.handle_toppings("mayo")


def test_patty_out_of_stock(machine): 
    # UCID is js2679 and date is  23/03/2023
    machine.patties[0].quantity = 0 
    with pytest.raises (OutOfStockException): 
        machine.handle_bun("lettuce wrap") 
        machine.handle_patty("turkey")


def test_if_toppings_out_of_stock(machine): 
    # UCID is js2679 and date is  23/03/2023
    machine.toppings[0].quantity = 0 
    with pytest.raises (OutOfStockException): 
        machine.handle_bun("lettuce wrap") 
        machine.handle_patty("turkey")
        machine.handle_patty("next")
        machine.handle_toppings("lettuce")


def test_if_patty_are_exceded (machine):
# UCID is js2679 and date is  23/03/2023 
    with pytest.raises (ExceededRemainingChoicesException): 
        machine.handle_bun("lettuce wrap")

        machine.handle_patty("beef")

        machine.handle_patty("veggie")

        machine.handle_patty("beef")

        machine.handle_patty("beef")

def test_if_toppings_are_exceded (machine): 
    # UCID is js2679 and date is  23/03/2023 
    with pytest.raises (ExceededRemainingChoicesException): 
        machine.handle_bun("lettuce wrap") 
        machine.handle_patty("beef") 
        machine.handle_patty("next") 
        machine.handle_toppings("bbq") 
        machine.handle_toppings("cheese")

        machine.handle_toppings("mayo")

        machine.handle_toppings("pickles")


def test_cost_of_burger (machine1): 
# UCID is js2679 and date is  23/03/2023    
    machine1.handle_bun( "no Bun") 
    machine1.handle_patty("veggie")
    machine1.handle_patty("veggie")
    machine1.handle_patty("next")
    machine1.handle_toppings("cheese") 
    machine1.handle_toppings("mustard")
    machine1.handle_toppings("done")
    total1= machine1.calculate_cost()
    assert total1 == 2.25
    assert "${:.2f}".format(total1) == "$2.25"
    machine1.handle_pay(total1,"${:.2f}".format(total1)) 

    machine1.handle_bun("lettuce wrap")
    machine1.handle_patty("beef")
    machine1.handle_patty("next")
    machine1.handle_toppings("done") 
    total2 =machine1.calculate_cost()
    assert total2 == 2.5
    assert "${:.2f}".format(total2) == "$2.50" 
    machine1.handle_pay(total2, "${:.2f}".format(total2))

    machine1.handle_bun("Wheat Burger Bun") 
    machine1.handle_patty("veggie")
    machine1.handle_patty("next")
    machine1.handle_toppings("pickles") 
    machine1.handle_toppings("done")
    total3 = machine1.calculate_cost() 
    assert total3 == 2.5
    assert "${:.2f}".format(total3)== "$2.50"
    machine1.handle_pay(total3, "${:.2f}".format(total3))

#python -m pytest BurgerMachine"""

def test_total_burgers (machine): 
# UCID is js2679 and date is  23/03/2023      
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("turkey") 
    machine.handle_patty("beef") 
    machine.handle_patty("next")
    machine.handle_toppings("cheese") 
    machine.handle_toppings("ketchup")
    machine.handle_toppings("done") 
    machine.handle_pay(100,"${:.2f}".format(100))
    machine.handle_bun("no bun") 
    machine.handle_patty("turkey")
    machine.handle_patty("next")
    machine.handle_toppings("bbq")
    machine.handle_toppings("done")
    machine.handle_pay(100,"${:.2f}".format(100))
    assert machine.total_burgers == 2

def test_total_sales(machine): 
# UCID is js2679 and date is  23/03/2023    
    machine.handle_bun("White Burger Bun")
    machine.handle_patty("veggie")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("mayo") 
    machine.handle_toppings("bbq")
    machine.handle_toppings("done")
    total1 = machine.calculate_cost() 
    machine.handle_pay(total1,"${:.2f}".format(total1))
    
    machine.handle_bun("lettuce wrap")
    machine.handle_patty("beef")
    machine.handle_patty("next")
    machine.handle_toppings("done")
    total2 = machine.calculate_cost() 
    machine.handle_pay(total2,"${:.2f}".format(total2))

    machine.handle_bun("Wheat Burger Bun") 
    machine.handle_patty("veggie")
    machine.handle_patty("next") 
    machine.handle_toppings("pickles")
    machine.handle_toppings("done")
    total3= machine.calculate_cost()
    machine.handle_pay(total3,"${:.2f}".format(total3))
    assert machine.total_sales == total1+total2+total3
