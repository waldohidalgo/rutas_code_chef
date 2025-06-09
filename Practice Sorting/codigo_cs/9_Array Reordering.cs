using System;

public class Test9
{
    public static void ArrayReordering()
    {
        // your code goes here
        int t = int.Parse(Console.ReadLine());
        for (int i = 0; i < t; i++)
        {
            int n = int.Parse(Console.ReadLine());
            int[] arr1 = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            int[] arr2 = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            Array.Sort(arr1, (a, b) => -a.CompareTo(b));
            Array.Sort(arr2);

            Console.WriteLine(string.Join(" ", arr1));
            Console.WriteLine(string.Join(" ", arr2));
        }
    }
}
