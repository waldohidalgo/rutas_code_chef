using System;
using System.Collections.Generic;

public class Test12
{
    static int CountMaxSubarray(int[] arr, int n, int k)
    {
        // your code goes here
        int[] left = new int[n];
        Stack<int> stack = new();
        for (int i = 0; i < n; i++)
        {
            while (stack.Count > 0 && arr[stack.Peek()] < k)
            {
                stack.Pop();
            }
            left[i] = (stack.Count > 0) ? stack.Peek() : -1;
            stack.Push(i);
        }


        stack.Clear();
        int[] right = new int[n];

        for (int i = n - 1; i >= 0; i--)
        {
            while (stack.Count > 0 && arr[stack.Peek()] <= k)
            {
                stack.Pop();
            }
            right[i] = (stack.Count > 0) ? stack.Peek() : n;
            stack.Push(i);
        }
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            if (arr[i] == k)
            {
                count += (i - left[i]) * (right[i] - i);
            }
        }

        return count;


    }

    public static void Main12()
    {
        int[] data = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int n = data[0];
        int k = data[1];
        int[] arr = Console.ReadLine().Split().Select(int.Parse).ToArray();

        int result = CountMaxSubarray(arr, n, k);
        Console.WriteLine(result);
    }
}
