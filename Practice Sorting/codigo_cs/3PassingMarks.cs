using System;

public class Test3
{
    public static void PassingMarks()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            string[] s = Console.ReadLine().Split(' ');
            int n = int.Parse(s[0]);
            int x = int.Parse(s[1]);

            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            // your code goes here
            Array.Sort(arr);
            Console.WriteLine(arr[arr.Length - x] - 1);
        }
    }
}
