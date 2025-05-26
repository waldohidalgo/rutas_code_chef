// See https://aka.ms/new-console-template for more information
using System;

class Program
{
    static void Main(string[] args)
    {
        int[] arr = [6, 5, 3, 1, 8, 7, 2, 4];
        Test19.RadixSort(arr);
        Console.WriteLine(string.Join(" ", arr));
    }
}
