using System;
using System.Collections.Generic;
using System.Linq;
public class Test11
{
    public static void NGE()
    {
        // your code goes here
        int n = int.Parse(Console.ReadLine());
        int[] arr = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        int[] res = Enumerable.Repeat(-1, n).ToArray();
        Stack<int> stack = new Stack<int>();
        for (int i = n - 1; i >= 0; i--)
        {
            while (stack.Count > 0 && stack.Peek() <= arr[i])
            {
                stack.Pop();
            }
            if (stack.Count > 0)
            {
                res[i] = stack.Peek();
            }
            stack.Push(arr[i]);
        }
        Console.WriteLine(string.Join(" ", res));

    }
}