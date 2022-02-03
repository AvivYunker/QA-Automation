import org.openqa.selenium.By;
import org.openqa.selenium.JavascriptExecutor;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;

public class theRiddlePractice {

	public static void main(String[] args) {
		WebDriver browser = new ChromeDriver();
		JavascriptExecutor js = (JavascriptExecutor) browser;
		browser.navigate().to("https://techstepacademy.com/trial-of-the-stones");
		
		WebElement riddleOfStoneTextField = browser.findElement(By.id("r1Input"));
		WebElement answerButton1 = browser.findElement(By.id("r1Btn"));
		riddleOfStoneTextField.sendKeys("rock");
		answerButton1.click();
		WebElement answer1 = browser.findElement(By.xpath("//*[@id=\"passwordBanner\"]/h4"));
		String answer1Text = answer1.getText();
		
		WebElement riddleOfSecretsTextField = browser.findElement(By.id("r2Input"));
		WebElement answer2Button = browser.findElement(By.id("r2Butn"));
		riddleOfSecretsTextField.sendKeys(answer1Text);
		answer2Button.click();
		WebElement answer2 = browser.findElement(By.xpath("//*[@id=\"successBanner1\"]/h4"));
		
//		js.executeScript("window.scrollBy(0,500)");
		WebElement merchant1Name = browser.findElement(By.cssSelector("#block-05ea3afedc551e378bdc > div > div:nth-child(18) > span > b"));
		WebElement merchant1Wealth = browser.findElement(By.cssSelector("#block-05ea3afedc551e378bdc > div > div:nth-child(18) > p"));
		WebElement merchant2Name = browser.findElement(By.cssSelector("#block-05ea3afedc551e378bdc > div > div:nth-child(20) > span > b"));
		WebElement merchant2Wealth = browser.findElement(By.cssSelector("#block-05ea3afedc551e378bdc > div > div:nth-child(20) > p"));
		WebElement richestMerchantAnswer = browser.findElement(By.id("r3Input"));
		WebElement answer3Button = browser.findElement(By.id("r3Butn"));
	
		String merchange1NameString = merchant1Name.getText();
		String merchant1WealthString = merchant1Wealth.getText();
		String merchange2NameString = merchant2Name.getText();
		String merchant2WealthString = merchant2Wealth.getText();
		String richestMerchant = "";
				
		if (Integer.parseInt(merchant1WealthString) > Integer.parseInt(merchant2WealthString)) {
			richestMerchant = merchange1NameString;
		} else if (Integer.parseInt(merchant1WealthString) > Integer.parseInt(merchant2WealthString)) {
			richestMerchant = merchange2NameString;
		} else {
			richestMerchant = "none";
		}
		
//		System.out.println("REACHED!");
		richestMerchantAnswer.sendKeys(richestMerchant);
		answer3Button.click();
		WebElement finalResults = browser.findElement(By.cssSelector("#successBanner2 > h4"));
		String finalResultsString = finalResults.getText();
		
		if (finalResultsString.equals("Success!")) {
			System.out.println("\nV\n");
		} else {
			System.out.println("\nX\n");
		}
	}
}
