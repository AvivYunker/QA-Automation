import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class sauceLabsTest {

	public static void main(String[] args) {
		WebDriver browser = new ChromeDriver();
		browser.navigate().to("https://www.saucedemo.com/");
//		JavascriptExecutor js = (JavascriptExecutor) browser;
//		browser.manage().window().maximize();
		
//		PAGE 1 (elements)
		WebElement userNameTextField = browser.findElement(By.id("user-name"));
		WebElement passwordTextField = browser.findElement(By.id("password"));
		WebElement loginButton = browser.findElement(By.id("login-button"));
		
//		PAGE 1 (actions)
		userNameTextField.sendKeys("standard_user");
		passwordTextField.sendKeys("secret_sauce");
		loginButton.click();
		
//		PAGE 2 (elements)
		try {
			Thread.sleep(3000);
		} catch (InterruptedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		WebElement sauceLabsBackpackAddToCartButton = browser.findElement(By.id("add-to-cart-sauce-labs-backpack"));
		WebElement sauceLabsBikeLightAddToCartButton = browser.findElement(By.id("add-to-cart-sauce-labs-bike-light"));
		WebElement sauceLabsBoltTShirtAddToCartButton = browser.findElement(By.id("add-to-cart-sauce-labs-bolt-t-shirt"));
		WebElement sauceLabsFleeceJacketAddToCartButton = browser.findElement(By.id("add-to-cart-sauce-labs-fleece-jacket"));
		WebElement sauceLabsOnesieAddToCartButton = browser.findElement(By.id("add-to-cart-sauce-labs-onesie"));
		WebElement sauceLabsRedTShirtAddToCartButton = browser.findElement(By.id("add-to-cart-test.allthethings()-t-shirt-(red)"));
		WebElement shoppingCartButton = browser.findElement(By.className("shopping_cart_link"));
		
//      PAGE 2 (actions)
		sauceLabsBackpackAddToCartButton.click();
		sauceLabsBikeLightAddToCartButton.click();
//		js.executeScript("window.scrollBy(0,400)");
		sauceLabsBoltTShirtAddToCartButton.click();
		sauceLabsFleeceJacketAddToCartButton.click();
		sauceLabsOnesieAddToCartButton.click();
		sauceLabsRedTShirtAddToCartButton.click();
//		js.executeScript("window.scrollBy(0,-400)");
		shoppingCartButton.click();
		
//		PAGE 3 (elements)
		WebElement checkoutButton = browser.findElement(By.id("checkout"));
		
//		PAGE 3 (actions)
		checkoutButton.click();
		
//		PAGE 4 (elements)
		WebElement firstNameTextField = browser.findElement(By.id("first-name"));
		WebElement lastNameTextField = browser.findElement(By.id("last-name"));
		WebElement postalCodeTextField = browser.findElement(By.id("postal-code"));
		WebElement continueButton = browser.findElement(By.id("continue"));
		
//		PAGE 4 (actions)
		firstNameTextField.sendKeys("first");
		lastNameTextField.sendKeys("last");
		postalCodeTextField.sendKeys("12345");
		continueButton.click();
		
//		PAGE 5 (elements)
		WebElement finishButton = browser.findElement(By.id("finish"));
		
//		PAGE 5 (actions)
		finishButton.click();
		
//		PAGE 6 (elements)
		WebElement successResult = browser.findElement(By.cssSelector("#checkout_complete_container > h2"));
		String successMessage = successResult.getText().toString();
		
		if (successMessage.equals("THANK YOU FOR YOUR ORDER")) {
			System.out.println("\nV\n");
		} else {
			System.out.println("\nX\n");
//			System.out.println("val: " + successMessage);
//			System.out.println("exp: " + "THANK YOU FOR YOUR ORDER");
		}
//		System.out.println("The text was: " + successMessage);
	}
}