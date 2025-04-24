using System;
using System.Linq;
using System.Collections.Generic;
public class Test19
{
    public static void Candies()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int _ = 0; _ < t; _++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr = Console.ReadLine().Split().Select(int.Parse).ToArray();
            Dictionary<int, int> dict = new Dictionary<int, int>();
            bool isPossible = true;
            for (int i = 0; i < 2 * n; i++)
            {
                if (dict.ContainsKey(arr[i]))
                {
                    dict[arr[i]]++;
                }
                else
                {
                    dict.Add(arr[i], 1);
                }

                if (dict[arr[i]] > 2)
                {
                    isPossible = false;
                    break;
                }
            }

            if (isPossible)
            {
                Console.WriteLine("Yes");
            }
            else
            {
                Console.WriteLine("No");
            }

        }

    }
}

