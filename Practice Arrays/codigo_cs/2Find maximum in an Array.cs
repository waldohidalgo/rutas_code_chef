using System;
using System.Linq;

class Test2
{
    static void GetMaximun()
    { 
        		// your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr = new int[n];
            int max=0;
            string[] input = Console.ReadLine().Split();
            for (int i = 0; i < n; i++)
            {
                arr[i] = int.Parse(input[i]);
                if (arr[i] > max)
                {
                    max = arr[i];
                }
            }
            Console.WriteLine(max);
        }
    }
}