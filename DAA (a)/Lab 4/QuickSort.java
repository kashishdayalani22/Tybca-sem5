public class QuickSort {

    static int[] quickSort(int[] arr) {
        if (arr.length <= 1) {
            return arr;
        }

        int pivot = arr[arr.length / 2];

        int[] left = new int[arr.length];
        int[] middle = new int[arr.length];
        int[] right = new int[arr.length];

        int l = 0, m = 0, r = 0;

        for (int x : arr) {
            if (x < pivot) {
                left[l++] = x;
            } else if (x == pivot) {
                middle[m++] = x;
            } else {
                right[r++] = x;
            }
        }

        int[] leftPart = new int[l];
        int[] middlePart = new int[m];
        int[] rightPart = new int[r];

        System.arraycopy(left, 0, leftPart, 0, l);
        System.arraycopy(middle, 0, middlePart, 0, m);
        System.arraycopy(right, 0, rightPart, 0, r);

        int[] sortedLeft = quickSort(leftPart);
        int[] sortedRight = quickSort(rightPart);

        int[] result = new int[arr.length];
        int index = 0;

        for (int x : sortedLeft) {
            result[index++] = x;
        }

        for (int x : middlePart) {
            result[index++] = x;
        }

        for (int x : sortedRight) {
            result[index++] = x;
        }

        return result;
    }

    public static void main(String[] args) {
        int[] numbers = {10, 7, 8, 9, 1, 5, 17, 4, 20};

        System.out.print("Original Array: ");
        for (int x : numbers) {
            System.out.print(x + " ");
        }

        int[] sortedNumbers = quickSort(numbers);

        System.out.print("\nSorted Array: ");
        for (int x : sortedNumbers) {
            System.out.print(x + " ");
        }
    }
}
