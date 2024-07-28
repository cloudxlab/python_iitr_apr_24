--
May 4th 2024

	Q1. create a Base X (eg:- 12,14,18) numering system. 
		- Write two digit numbers in that number system.
		- Perform Sigle digit addition
		- Perform double digit addition.
		- Multipliaction table for 1-10 in this number system.
		- Perform double digit multiplication.
		- Convert from Base X to Base 10
		- Convert from Base 10 to Base X
--
May 11th and 12th 2024

	Q1. Calculate grosspay given hours and rate
	Q2. Rewrite the pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours
	Q3. Write a program to compute the total amount after compounded interest

		Principle: Rate: Time (year):
		Print the total amount after applying compound interest.
		Total = Principle * (1 + rate/100)**years
	Q4. Print all strings that can be generated from a list of letters.
		Input: abc
		Output:
		abc
		acb
		bac
		bca
		cab
		cba
	Q5. BLEU Score. Code it
		
		Bleu(N) =Brevity Penalty * Geometric Average Precision scores
		c= predicted length
		r= target length

		Brevity Penalty 	
			   =1 , if c>r 
			   =e**(1-r/c) , if c<=r
			   
		Geometric Average Precision scores = p1**(1/4) * p2**(1/4)  *p3**(1/4) * p4**(1/4)
	Q6. Code multiplication without using * or loops
--
May 18th and 19th 2024

	Q1. Code Tower of Hanoi Problem
	Q2. Write a wild card character matcher. * matches 0 or more chars. ? matches only one character.

		a* -> abc, ab, ax, a 
		a? -> a1, a2, aa,
		a*b -> axyzb, a123b, ab
		a*b*c -> abc, abbbc, a1b1c
		aa?b*:
			match: aa1b, aaxby, aa1bcdeffgshshshsh
			not match: aab, ab,
		def ismatch(pat, text):
			return True/False
	
	Q3. Given two vectors (arrays or list of numbers)

		return the difference of the two vectors
		diff([1,2,3], [2,3,4]) => [-1, -1, -1]
	Q4. Given two vectors (arrays or list of numbers). Find absolute distance between them. L1 Distance.

		abs_distance([1,2,3], [2, 3, 4]) -> 3
		abs_distance([5,4,1], [2, 3, 4]) -> 3+1+3 = 7
	Q5. Given two 2D vectors representing two points, find the distance between two points.

		distance([1,2], [3,5]) -> sqrt((3 - 1)**2 + (5-2)**2)
			sqrt(13) = 3.605551275463989
	Q6. Given two 3D vectors representing two points, find the distance between two points. distance3d([1, 2, 3], [2,3,4] ) -> math.sqrt(3)

	Q7. Generalize problem Q4 for n dimensions.
--
May 25th and 26th 2024

	Q1. Coin Toss: Create a function that return 0 or 1 with equal probability. Hint: random.random()
	Q2. Coin Toss: Create a function that return 0, 1, 2 with equal probability.
	Q3. Create a n faced die which generates number from 0 to n - 1 with equal probability.
	Q4. Unfair Coin:
		def coin_toss(p1, p2): # p1 /(p1 + p2), p2/(p1+p2) # return 0 p1 probability # return 1 with p2 probability
	Q5. coin_toss, takes three probability p1, p2, p3 as arguments.
		Return 0 with p1 probability. 1 with p2 probability. 2 with p3 probability. coin_toss_3(0.7, 0.2, 0.1) # 0 - 70% of times, 1 - 20% of time, 2 - 10% of time
	Q6. Generalize coin_toss, takes n probability p1, p2, p3..pn-1 as arguments.
--
June 1st and 2nd 2024

	Q1. Code the SQRT
	Q2. Code the 1/4 power?
	Q3. Code the 1/5 power
	Q4. Convert to probability
		10, 20, 30 -> 10/(10+20+30), 20/(10+20+30), 30/(10+20+30)
	Q5: Softmax
		[1,2,3] -> 10^1, 10^2, 10^3 -> convert_to_prob 
--
June 7th and 8th 2024

	Q1. Given array of sorted numbers, check if a number exists in them. Mention the time complexity
		- using loops
		- using recursion
	Q2. You have a list of 0s and 1s....find the count of 0s. the array is sorted. Mention the time complexity
		count_zeros([0,0,0,0,0,1,1,1,1,1,1]) -> 5
	Q3. Count 1s in a sorted array of numbers. Mention complexity
		count_ones([0,0,0,0,0,1,1,1,1,1,1,1.1, 1.2, 2]) ->6
	Q4. Given a number represented as string convert it integer. Mention time Complexity
		to_num("145") -> 145
	Q5. You have two lists of numbers:
		First list: 100 numbes. not sorted m
		Second List: Millions of numbers. not sorted n
		Find all numbers which are common in these two lists
		Mention time complexity.
--
June 14th and 15th 2024

	Q1. Rewrite this code to make it using circular buffer
		read a line
		append a line
		if size of the buffer is > 10, knock out the first
		last_n_lines(file_name, num=10)
		
	Q2. Write a program to simulate circular buffer
		circle_append(lst, element)	
		
	Q3. Find Longest Line in the file
	Q4. Implement last_n_lines method using traversing
	Q5. Find the frequency of words in a file
	Q6. Checkout the animations and try to code them and calculate their complexity.
			- BubbleSort
			- Insertion Sort
			- MergeSort
			- QuickSort
--
June 22nd and 23rd 2024

	Q1. Write code to solve equations
	
--
July 6th and 7th 2024

	Q1. [(0,"x"), (1, 12), (0, 34), (1,90), (1,89), (0,"s"), (1, "7")]
		Move all zeros to the begining and all 1s to end without using another list in order of n
		Input: [(0,"x"), (1, 12), (0, 34), (1,90), (1,89), (0,"s"), (1, "7")]
		Expected Output: [(0,"x"), (0, 34), (0,"s"), (1,89), (1,90), (1, 12), (1, "7")]
		
	Q2. Counting Sort:
		Sort the numbers containing age of people. Billion numbers.
		I maintain an array of 200 numbers. 0th index is for people with 0 yrs....
		200th elements contains count of people with 200 age.
	Q3. Attempt the encode and decorder problem in problem.pdf
		- dictionary approach
		- without dictionary approach
--
July 13th and 14th 2024

	Q1. Implement Binary Search Tree Delete (Insert and Find done in class)
	
--
July 20th and 21st 2024

	https://docs.python.org/3/library/heapq.html
	Q1. Check out Traversal of Tree
			- Depth first
			- Breath First
	Q2.Implement a simple pattern matcher that matches . with single character and * with any number (0 or more) of any character
	Q3: Write regular expression to match email address
	Q4: Write regular expression to match URL
	Q5: Build a regular expression to extract URLs from the server logs 'access.log.41'

--
July 27th and 28th 2024

	Go through the below blog on sentiment Analysis
	https://cloudxlab.com/blog/understanding-embeddings-and-matrices-with-the-help-of-sentiment-analysis-and-llms-hands-on/
	
	code available in below repo
	https://github.com/cloudxlab/Hands-On-LLMs-with-OpenAI-and-Langchain/blob/main/Sentiment%20Analysis%20with%20LLMs/Sentiment%20Analysis%20with%20LLMs.ipynb
    
    
