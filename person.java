class person 
{
	int age=19;
	int wgt=45;
	int hgt=5;

	
	void walk()
	{
		System.out.println("today i walk 4 km");
	}
	void eat()
	{
	 	System.out.println("i eat pavbhaji in breakfast");
	}
	
	public static void main(String[] args){
		System.out.println("hellow my name is sharvari");
		person p=new person();
		p.walk();
		p.eat();
		System.out.println("my age is "+p.age);
		System.out.println("my weight is "+p.wgt);
		System.out.println("my hight is "+p.hgt);
	}
}