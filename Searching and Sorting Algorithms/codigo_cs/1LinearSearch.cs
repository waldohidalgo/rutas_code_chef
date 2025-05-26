using System;
using System.Linq;
public class Test1
{
    public static void LinearSearch()
    {
        // your code goes here
        string input = Console.ReadLine();
        int n = int.Parse(input.Split(' ')[0]);
        int k = int.Parse(input.Split(' ')[1]);
        int[] arr = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        bool isFound = false;
        for (int i = 0; i < n; i++)
        {
            if (arr[i] == k)
            {
                Console.WriteLine("Yes");
                isFound = true;
                break;
            }
        }
        if (!isFound)
        {
            Console.WriteLine("No");
        }

    }
}
