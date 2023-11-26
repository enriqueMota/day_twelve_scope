############ Scope #############

# enemies: int = 1


# def increase_enemies():
    #? This is not in the scope so enemies would be a new variable
    # enemies: int = 2
    # print(f"enemies inside function: {enemies}")

#? Here, enemies is still 1 because inside the function it is not affected
# increase_enemies()
# print(f"enemies ouside function: {enemies}")


#? Local scope

# def drink_potion():
    #? This is only accesible inside this function
    # potion_strenght = 2
    # print(potion_strenght)
    
# drink_potion()
#? this wouldn't work here because it doesn't exist in the scope
# print(potion_strength)


#? Global scope
# player_health = 10
# def drink_potion():
    # potion_strenght = 2
    #? Player health will be available here because it is in the global scope
    # print(player_health)

# drink_potion()


#? if statements variables are not block scoped, meaning they are global if outside a function


enemies = 1

def increase_enemies():
    #? In order to reference a variable outside the scope or a global variable
    #? We should add "global" to specify it's the global one
    #! This is not recommended
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")