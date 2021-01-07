import java.util.Scanner;

public class complementBinary {
	public static void main(String[] args) {
	String complementor = "";
	int dec = 0;
	
		Scanner sc = new Scanner(System.in);
			String binary = sc.nextLine();
		for(int i = 0; i<binary.length();i++) {
			String v = Character.toString(binary.charAt(i));
			if(v.equals("0")) {
					complementor = complementor.concat("1");
				}
				if(v.equals("1")) {
					complementor = complementor.concat("0");
				}	
				
			}
		
		System.out.println("the complement of "+ binary +" is: "+  complementor);
			System.out.println(binary+"="+Integer.parseInt(binary,2));
				System.out.println(complementor+"="+Integer.parseInt(complementor,2));
		
		
	}
}
