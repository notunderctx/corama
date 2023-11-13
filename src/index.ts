import figlet from "figlet";
import * as readline from "readline";

function input(question: string) {
  const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
  });

  return new Promise<string>((resolve) => {
    rl.question(question, (answer) => {
      rl.close();
      resolve(answer);
    });
  });
}

interface Scii {
  text: string;
}

function ascii(data: Scii): Promise<void> {
  return new Promise<void>((resolve, reject) => {
    figlet.text(
      `${data.text}`,
      {
        font: "Ghost",
        horizontalLayout: "default",
        verticalLayout: "default",
        width: 80,
        whitespaceBreak: true,
      },
      function (err, asciiArt) {
        if (err) {
          reject(err);
        } else {
          console.log(asciiArt);
          resolve();
        }
      }
    );
  });
}

async function main() {
  const ty = await input("Enter some text: ");
  await ascii({
    text: `${ty}`,
  });
}

main().catch((error) => {
  console.error("Error:", error);
});
