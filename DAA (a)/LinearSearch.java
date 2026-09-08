public class LinearSearch{
    public static void main(String[] args){
        int target = 5;
        int[] arr = {1, 2, 4, 5, 7, 8, 9, 10};
        boolean found = false;
        for(int i : arr){
            if(i == target){
                found = true;
                System.out.println("Target found at" + index[i] + "of array");
                break;
            }
        }

        if(!found){
            System.out.println("Target not in array");
        }
    }
}
