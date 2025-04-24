using System;
using System.Linq;

class Test1
{
    static void SearchElement()
    {
        string[] input = Console.ReadLine().Split();
        int n = int.Parse(input[0]);
        int x = int.Parse(input[1]);

        int[] arr = Console.ReadLine().Split().Select(int.Parse).ToArray();

        foreach (int el in arr)
        {
            if (el == x)
            {
                Console.WriteLine("YES");
                return;
            }
        }
        Console.WriteLine("NO");
    }
}
