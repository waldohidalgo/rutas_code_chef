using System;

class Test5
{
    static void MinumumOperations()
    {
        int t = int.Parse(Console.ReadLine()); // Read the number of test cases
        while (t-- > 0)
        {
            int n = int.Parse(Console.ReadLine()); // Read the size of the array
            int[] a = new int[n]; // Declare the array with size n
            
            // Read the array elements in a single line
            string[] input = Console.ReadLine().Split();

            int min=0;
            for (int i = 0; i < n; i++)
            {
                a[i] = int.Parse(input[i]); // Parse the input elements into the array
                if (a[i]<min) min=a[i];
            }
            
            // Your code goes here
            int count=0;
            for (int i = 0; i < n; i++){
                if(min!=a[i]) count++;
            }
            Console.WriteLine($"count: {count}");
            
        }
    }
}
