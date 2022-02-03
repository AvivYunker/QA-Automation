import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class xpathSelectorExample {

	public static void main(String[] args) {
		WebDriver browser = new ChromeDriver();
		
		browser.navigate().to("https://techstepacademy.com/training-ground");
//		elements
		WebElement textInputField1 = browser.findElement(By.xpath("//*[@id=\"ipt1\"]"));
		WebElement textInputField2 = browser.findElement(By.xpath("//*[@id=\"ipt2\"]"));
		WebElement button1 = browser.findElement(By.xpath("//*[@id=\"b1\"]"));
		WebElement button2 = browser.findElement(By.xpath("//*[@id=\"b2\"]"));
		WebElement button3 = browser.findElement(By.xpath("//*[@id=\"b3\"]"));
		WebElement button4 = browser.findElement(By.xpath("//*[@id=\"b4\"]"));
		
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
