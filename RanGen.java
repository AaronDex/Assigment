//Does random gen for ints and boolean
public class RanGen {
  public static int NumGen(){
       //instance of random class
      if (BooleanGen() == true){
        
        int min = 100000;
        int max = 199999;
        
        int rand_int = (int)Math.floor(Math.random()*(max-min+1)+min);
        System.out.print(Input.InputName()+"'s "+"Ticket ID Is: " + rand_int + " Is Genuine Part");
        return rand_int;
        
        
      }else{
        int min = 200000;
        int max = 299999;

        int rand_int = (int)Math.floor(Math.random()*(max-min+1)+min);
        System.out.print(Input.InputName()+"'s "+"Ticket ID Is: " + rand_int +" Not Genuine Part"  );
        
        return rand_int;}
      
  }
  public static  boolean BooleanGen() {
     boolean Gen = Math.random() < 0.5;

    return Gen;
  }
}