public class practice{
    
    public static void main(String[] args){

        String[][] a = {{"1", "2", "3", "4"}, {"5", "6", "7", "8"}, {"9", "10", "11", "12"}};
        String[] b = {"9", null, "11"};


        dance: for(int i = 0; i < a.length; i++){

            System.out.println(i);

            for(int j = 0; j < b.length; j++){


               if(b[j] != null){
                if(b[j] != a[i][j]){
                    continue dance;
                }
            }
            }

            System.out.println("hello");
            System.out.println(i);
        }
    }
}