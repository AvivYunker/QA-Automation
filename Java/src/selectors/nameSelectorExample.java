import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class nameSelectorExample {

	public static void main(String[] args) {
		WebDriver browser = new ChromeDriver();
		
		browser.navigate().to("https://techstepacademy.com/training-ground");
//		elements
		WebElement textInputField1 = browser.findElement(By.name("Input 1"));
		WebElement textInputField2 = browser.findElement(By.name("Input 2"));
		WebElement button1 = browser.findElement(By.name("butn1"));
		WebElement button2 = browser.findElement(By.name("butn2"));
		WebElement button3 = browser.findElement(By.name("butn3"));
		WebElement button4 = browser.findElement(By.name("butn4"));
		
//		actions
		textInputField1.sendKeys("sample text...");
		button1.click();
		browser.switchTo( ).alert( ).dismiss();
		button2.click();
		browser.switchTo( ).alert( ).dismiss();
		
		textInputField2.sendKeys("sample text...");
		button3.click();
		browser.switchTo( ).alert( ).dismiss();
		button4.click();
		browser.switchTo( ).alert( ).dismiss();
	}
}
