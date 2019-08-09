import javax.swing.*;  
import java.awt.*;  
import java.awt.event.*;  
public class PayrollMgnt {  
public static void main(String[] args) {  
JFrame f=new JFrame("Payroll Management system");//creating instance of JFrame 
JLabel l1,l2,l3,l4,l5,l6,l7,l8,l9,l10; 
JTextField tf1,tf2,tf3,tf4,tf5,tf6,tf7,tf8,tf9,tf10; 
 JTextArea area=new JTextArea();  
 area.setBounds(700,30, 200,400);  
 f.add(area);  
    l1=new JLabel("Name:");  
    l1.setBounds(0,50, 100,30); 
    tf1=new JTextField();  
    tf1.setBounds(100,50, 100,20);	
    l2=new JLabel("Address:");  
    l2.setBounds(400,50, 100,30); 
	tf2=new JTextField();  
    tf2.setBounds(500,50, 100,20);
	l3=new JLabel("Employer:");  
    l3.setBounds(0,100, 100,30);
	tf3=new JTextField();  
    tf3.setBounds(100,100, 100,20);
	l4=new JLabel("E-Number:");  	
    l4.setBounds(400,100, 100,30);
	tf4=new JTextField();  
    tf4.setBounds(500,100, 100,20);
	l5=new JLabel("Hours Worked:");  
    l5.setBounds(0,150, 100,30);
	tf5=new JTextField();  
    tf5.setBounds(100,150, 100,20);
	l6=new JLabel("Hourly Rate:");  
    l6.setBounds(400,150, 100,30);
	tf6=new JTextField();  
    tf6.setBounds(500,150, 100,20);
	l7=new JLabel("Tax:");  
    l7.setBounds(0,200, 100,30);
	tf7=new JTextField();  
    tf7.setBounds(100,200, 100,20);
	l8=new JLabel("OverTime:");  
    l8.setBounds(400,200, 100,30);
	tf8=new JTextField();  
    tf8.setBounds(500,200, 100,20);
	l9=new JLabel("Gross Pay:");  
    l9.setBounds(0,250, 100,30);
	tf9=new JTextField();  
    tf9.setBounds(100,250, 100,20);
	l10=new JLabel("Net Pay:");  
    l10.setBounds(400,250, 100,30);
	tf10=new JTextField();  
    tf10.setBounds(500,250, 100,20);
f.add(tf1);f.add(tf2); f.add(tf3); f.add(tf4); f.add(tf5); f.add(tf6); f.add(tf7); f.add(tf8); f.add(tf9); f.add(tf10);f.add(l1); f.add(l2);f.add(l3); f.add(l4); f.add(l5); f.add(l6); f.add(l7); f.add(l8); f.add(l9); f.add(l10);       
JButton b=new JButton("Weekly Salary");//creating instance of JButton  
b.setBounds(0,400,100, 40);//x axis, y axis, width, height  
JButton c=new JButton("Reset");//creating instance of JButton  
c.setBounds(150,400,100, 40);
JButton d=new JButton("View Payslip");//creating instance of JButton  
d.setBounds(300,400,100, 40);
JButton e=new JButton("Exit System");//creating instance of JButton  
e.setBounds(500,400,100, 40);
f.add(b);//adding button in JFrame  
f.add(c);
f.add(d);
f.add(e);	  
f.setSize(1000,500);//400 width and 500 height  
f.setLayout(null);//using no layout managers  
f.setVisible(true);//making the frame visible 
e.addActionListener(new ActionListener() {
 public void actionPerformed (ActionEvent e) {
  System.exit(0);
 }
});
c.addActionListener(new ActionListener(){
public void actionPerformed(ActionEvent e){
tf1.setText(" ");
tf2.setText(" ");
tf3.setText(" ");
tf4.setText(" ");
tf5.setText(" ");
tf6.setText(" ");
tf7.setText(" ");
tf8.setText(" ");
tf9.setText(" ");
tf10.setText(" ");
}
});
b.addActionListener(new ActionListener(){
 public void actionPerformed(ActionEvent e) {  
 String s1=tf5.getText();  
 String s2=tf6.getText();  
 int a=Integer.parseInt(s1);  
 int b=Integer.parseInt(s2);  
    int o=0;
    if (a>40)
	o= a-40;
      int c=(a-o)*b+(o*500);
	  double tax=c*0.05;
	  double netpay=c-tax;
	    String result3=String.valueOf(o);
        String result=String.valueOf(c);  
		String result1=String.valueOf(tax);  
		String result2=String.valueOf(netpay);  
        tf9.setText(result);  
		tf7.setText(result1);  
		tf10.setText(result2);
		tf8.setText(result3);
		
    } 
});	
d.addActionListener(new ActionListener(){
public void actionPerformed(ActionEvent e){
area.setText(" ");
 String s1=tf1.getText();  
 String s2=tf2.getText();  
 String s3=tf3.getText();  
 String s4=tf4.getText();  
 String s5=tf5.getText();  
String s6=tf6.getText();  
String s7=tf7.getText();  
String s8=tf8.getText();  
String s9=tf9.getText();  
String s10=tf10.getText(); 
 String s11=l1.getText(); 
 String s12=l2.getText(); 
 String s13=l3.getText(); 
 String s14=l4.getText(); 
 String s15=l5.getText(); 
 String s16=l6.getText(); 
String s17=l7.getText(); 
String s18=l8.getText(); 
String s19=l9.getText(); 
String s20=l10.getText(); 
area.append("PaySlip"+"\n"+s11+s1+"\n"+s12+s2+"\n"+s13+s3+"\n"+s14+s4+"\n"+s15+s5+"\n"+s16+s6+"\n"+s17+s7+"\n"+s18+s8+"\n"+s19+s9+"\n"+s20+s10+"\n"+"copyright@aditi");
}
});
}  
}