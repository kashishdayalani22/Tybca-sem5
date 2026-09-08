public class BinarySearch {
    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 5, 7, 8, 9, 10}; // array must be sorted in binary search
        int target = 7;
        int low = 0;                           // starting index of the array
        int high = arr.length - 1;             // ending index of the array
        // length se index banane ke liye -1
        boolean found = false;

        while (low <= high) {
            int mid = (low + high) / 2;     //finding the mid index
            if (arr[mid] == target) {
                found = true;
                System.out.println("Target found in array");
                break;
            } else if (arr[mid] < target) {     // look in right or greater half
                low = mid + 1;                  // updating starting index
            } else {                // look in left or smaller half
                high = mid - 1;     // updating ending index
            }
        }

        if (!found) {
            System.out.println("Target not in array");
        }
    }
}
