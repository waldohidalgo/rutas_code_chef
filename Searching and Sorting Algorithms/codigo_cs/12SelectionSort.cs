using System;

class Test12
{
    static void SelectionSort(int[] arr, int n)
    {
        // write your code here
        for (int i = 0; i < n; i++)
        {
            int min_index = i;
            for (int j = i + 1; j < n; j++)
            {
                if (arr[j] < arr[min_index])
                {
                    min_index = j;
                }
            }

            int temp = arr[min_index];
            arr[min_index] = arr[i];
            arr[i] = temp;
        }

        Console.WriteLine(string.Join(" ", arr));

    }

    public static void Execute12()
    {
        int n = int.Parse(Console.ReadLine());
        int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
        SelectionSort(arr, n);
    }
}