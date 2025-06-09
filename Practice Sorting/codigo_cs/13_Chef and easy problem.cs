using System;

public class Test13
{
    public static void EasyProblem()
    {
        int t = int.Parse(Console.ReadLine());
        for (int j = 0; j < t; j++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            Array.Sort(arr);
            long count = 0; // si utilizo int se alcanza el limite maximo de int
            for (int i = n - 1; i >= 0; i -= 2)
            {
                count += arr[i];
            }
            Console.WriteLine(count);
        }
    }
}
