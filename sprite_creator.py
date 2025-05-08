from time import sleep as bake_time
import tsapp
import os

def get_sprites(window, images, pizzas):
    oven = tsapp.Sprite("/app/images/Forge.png", 250, 200, 1.0)
    window.add_object(oven)
    
    bowl = tsapp.Sprite("/app/images/Washpan.png", 650, 400, 1.0)
    window.add_object(bowl)
    
    uncooked_pizza = tsapp.Sprite("/app/images/PizzaWhole.png", 690, 285, 0.5)
    window.add_object(uncooked_pizza)
    pizzas.append(uncooked_pizza)
    uncooked_pizza.visible = False
    
    baked_pizza = tsapp.Sprite("/app/images/PizzaWholeBig.png", 350, 300, 0.3)
    window.add_object(baked_pizza)
    pizzas.append(baked_pizza)
    baked_pizza.visible = False
        
    dough = tsapp.Sprite("/app/images/Dough.png", 320, 40, 0.5)
    window.add_object(dough)
    images.append(dough)
    
    pepperoni = tsapp.Sprite("/app/images/HamSlice.png", 500, 220, 0.5)
    window.add_object(pepperoni)
    images.append(pepperoni)
    
    cheese = tsapp.Sprite("/app/images/CheeseSlice.png", 20, 60, 0.5)
    window.add_object(cheese)
    images.append(cheese)
    
    sauce = tsapp.Sprite("/app/images/Ketchup.png", 200, 115, 0.5)
    window.add_object(sauce)
    images.append(sauce)
    
    return oven, bowl, uncooked_pizza, baked_pizza

def drag_all_if_clicked(sprites, mouse_x, mouse_y):
    for sprite in sprites:
        if sprite.is_colliding_point(mouse_x, mouse_y) and tsapp.is_mouse_down():
            sprite.center_x, sprite.center_y = mouse_x, mouse_y

def bake_timer():
    [bake_time(0.65) or print("Baking\n") for i in range(4) if True]
    print("Done!\n")
    bake_time(1.00)