using System;
using System.Linq;
public class Test13
{
    public static void IS()
    {
        // your code goes here
        int n = int.Parse(Console.ReadLine());
        int[] arr = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);


        for (int i = 1; i < n; i++)
        {
            int curr = arr[i];
            int j = i - 1;
            while (j >= 0 && arr[j] > curr)
            {
                arr[j + 1] = arr[j];
                j--;
            }
            arr[j + 1] = curr;
        }
        Console.WriteLine(string.Join(" ", arr));

    }
}