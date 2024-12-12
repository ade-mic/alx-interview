#!/usr/bin/python3
"""
Maria and Ben are playing a game. Given a set of consecutive
integers starting from 1 up to and including n,
they take turns choosing a prime number from the set and removing that number
and its multiples from the set.
The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round.
Assuming Maria always goes first and both players play optimally,
determine who the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
"""



def sieve_of_eratosthenes(max_n):
    """
    Helper function to generate primes up to the maximum number in nums
    """
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not prime
    for p in range(2, int(max_n**0.5) + 1):
        if primes[p]:
            for multiple in range(p * p, max_n + 1, p):
                primes[multiple] = False
    return primes

def isWinner(x, nums):
    """
    Returns the winner of prime number game
    Args:
        x(int): number of rounds
        nums(list): Array of n
    Returns:
        returns name of player that won the most rounds
        if the winner cannot be determined return None
        n and x will not be longer than 10000
    """
    if x < 1 or not nums:
        return None
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    # count the number of primes up to each number
    prime_counts = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_counts[i] = prime_counts[i -1] + (1 if primes[i] else 0)
     
    maria_wins = 0
    ben_wins = 0
    player2 = "Ben"
    for n in nums:
        # Maria wins if the count is odd
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            # Ben wins if the count is even
            ben_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None