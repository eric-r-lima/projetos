{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "6e80eb7f-3dca-42cb-8ed6-f0099ad0a163",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "==========================\n",
      "Bem vindo ao jogo Papel, Pedra e Tesoura\n",
      "==========================\n",
      "\n",
      "PLACAR:\n",
      "Você: 0\n",
      "Computador: 0\n",
      "\n",
      "\n",
      "Escolha seu lance:\n",
      "0 - Papel | 1 - Pedra | 2 - Tesoura\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 1\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'p_move' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[27], line 67\u001b[0m\n\u001b[0;32m     65\u001b[0m player_move \u001b[38;5;241m=\u001b[39m get_player_move()\n\u001b[0;32m     66\u001b[0m computer_move \u001b[38;5;241m=\u001b[39m select_move()\n\u001b[1;32m---> 67\u001b[0m winner \u001b[38;5;241m=\u001b[39m select_winner(\u001b[43mp_move\u001b[49m, c_move)\n\u001b[0;32m     69\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m \u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     70\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m==========================\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'p_move' is not defined"
     ]
    }
   ],
   "source": [
    "import random\n",
    "import os\n",
    "\n",
    "move=[\"papel\", \"pedra\", \"tesoura\"]\n",
    "player_count = 0\n",
    "computer_count = 0\n",
    "\n",
    "print(\"==========================\")\n",
    "print(\"Bem vindo ao jogo Papel, Pedra e Tesoura\")\n",
    "\n",
    "def main_print():\n",
    "    print(\"==========================\")\n",
    "    print(\"\\nPLACAR:\")\n",
    "    print(\"Você: {}\".format(player_count))\n",
    "    print(\"Computador: {}\".format(computer_count))\n",
    "    print(\"\\n\")\n",
    "    print(\"Escolha seu lance:\")\n",
    "    print(\"0 - Papel | 1 - Pedra | 2 - Tesoura\")\n",
    "\n",
    "def select_move():\n",
    "    return random.choice(move)\n",
    "\n",
    "def get_player_move():\n",
    "    while True:\n",
    "        try:\n",
    "            player_move = int(input())\n",
    "            if player_move not in [0,1,2]:\n",
    "                raise\n",
    "            return move[player_move]\n",
    "        except Exception as e:\n",
    "            print(e)\n",
    "            \n",
    "def select_winner(p_move, c_move):\n",
    "    global player_count, computer_count\n",
    "    if p_move == \"papel\":\n",
    "        if c_move == \"pedra\":\n",
    "            player_count +=1\n",
    "            return \"p\"\n",
    "        elif c_move == \"tesoura\":\n",
    "            computador_count +=1\n",
    "            return \"c\"\n",
    "        else:\n",
    "            return \"d\"\n",
    "    if p_move == \"pedra\":\n",
    "        if c_move == \"tesoura\":\n",
    "            player_count +=1\n",
    "            return \"p\"\n",
    "        elif c_move == \"papel\":\n",
    "            computador_count +=1\n",
    "            return \"c\"\n",
    "        else:\n",
    "            return \"d\"\n",
    "    if p_move == \"tesoura\":\n",
    "        if c_move == \"papel\":\n",
    "            player_count +=1\n",
    "            return \"p\"\n",
    "        elif c_move == \"pedra\":\n",
    "            computador_count +=1\n",
    "            return \"c\"\n",
    "        else:\n",
    "            return \"d\"\n",
    "again = 1\n",
    "while again ==1:\n",
    "    main_print()\n",
    "    player_move = get_player_move()\n",
    "    computer_move = select_move()\n",
    "    winner = select_winner(player_move, computer_move)\n",
    "    \n",
    "    print(\" \")\n",
    "    print(\"==========================\")\n",
    "    print(\"Sua jogada: {}\",format(player_move.upper()))\n",
    "    print(\"Jogada do computador: {}\".format(computer_move.upper()))\n",
    "        \n",
    "    if winner == \"p\":\n",
    "        print(\"Você venceu!\")\n",
    "    elif winner == \"c\":\n",
    "         print(\"Você perdeu!\")\n",
    "    else:\n",
    "        print(\"Empate\")\n",
    "    print(\"==========================\")\n",
    "    \n",
    "    while True:\n",
    "        print(\"Jogar Novamente? 0 - Sim | 1 - Não\")\n",
    "        next = int(input())\n",
    "        if next == 0:\n",
    "            break\n",
    "        elif next ==1:\n",
    "            again = 0\n",
    "            break\n",
    "    os.system(\"cls\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c1d28b82-cfb5-40f6-b482-8572ec5cbb06",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
