{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bowling, BatingBowling\n",
      "player is going to bowl\n",
      "The count is added to computer\n"
     ]
    }
   ],
   "source": [
    "import random \n",
    "list1=[]\n",
    "list2=[]\n",
    "t=[1,2,3,4,5,6]\n",
    "\n",
    "\n",
    "\n",
    "player=input(\"Bowling, Bating\")\n",
    "if player==\"Bating\":\n",
    "        print(\"Computer is going to bowl\")\n",
    "        print(\"The count is added to player\")\n",
    "        \n",
    "        while True:\n",
    "            \n",
    "            player=int(input(\"Enter your numbers from 1 to 6\"))\n",
    "            computer=t[random.randint(0,5)]\n",
    "            print(computer)\n",
    "            list1.append(player)\n",
    "            print(\"sum of player:\",sum(list1))\n",
    "            list2.append(computer)\n",
    "            print(\"sum of computer:\",sum(list2))\n",
    "            \n",
    "            if player==computer:\n",
    "                print(\"the match is tie\")\n",
    "                list3=list1+list2\n",
    "                print(\"Total count of player is:\",sum(list3))\n",
    "                \n",
    "                break\n",
    "            else:\n",
    "                print(\"the match is not tie\")\n",
    "               \n",
    "        \n",
    "else:\n",
    "        print(\"player is going to bowl\")\n",
    "        print(\"The count is added to computer\")\n",
    "        while True:\n",
    "             player=int(input(\"Enter your numbers from 1 to 6\"))\n",
    "             computer=(int(t[random.randint(1,6)]))\n",
    "             print(computer)\n",
    "             list1.append(player)\n",
    "             print(\"sum of player:\",sum(list1))\n",
    "             list2.append(computer)\n",
    "             print(\"sum of computer:\",sum(list2))\n",
    "            \n",
    "             if player==computer:\n",
    "                print(\"the match is tie\")\n",
    "                list3=list1+list2\n",
    "                print(\"Total count of computer is:\",sum(list3))\n",
    "                \n",
    "                break\n",
    "             else:\n",
    "                print(\"the match is not tie\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
