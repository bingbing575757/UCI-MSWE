//// The primary purpose is to handle the logic of sending emails, and the Worker class receives and stores the SMTP server information required for sending emails.


// Library imports.
import Mail from "nodemailer/lib/mailer";
import * as nodemailer from "nodemailer";
import { SendMailOptions, SentMessageInfo } from "nodemailer";

// App imports.
import { IServerInfo } from "./ServerInfo";


// The worker that will perform SMTP operations.
export class Worker {


  // Server information.
  private static serverInfo: IServerInfo;


  /**
   * Constructor.
   */
  constructor(inServerInfo: IServerInfo) {

    console.log("SMTP.Worker.constructor", inServerInfo);
    Worker.serverInfo = inServerInfo;

  } /* End constructor. */


  /**
   * Send a message.
   *
   * @param  inOptions An object containing to, from, subject and text properties (matches the IContact interface,
   *                   but can't be used since the type comes from nodemailer, not app code).
   * @return           A Promise that eventually resolves to a string (null for success, error message for an error).
   */
  public sendMessage(inOptions: SendMailOptions): Promise<string> {

    console.log("SMTP.Worker.sendMessage()", inOptions);

    return new Promise((inResolve, inReject) => {
      const transport: Mail = nodemailer.createTransport(Worker.serverInfo.smtp);
      //Calls nodemailer.createTransport() method, passing the server information to establish a connection with the SMTP server.
      transport.sendMail(
        //Calls transport.sendMail() method, passing in the detailed message information inOptions received from the client.
        inOptions,
        (inError: Error | null, inInfo: SentMessageInfo) => {
          if (inError) {
            console.log("SMTP.Worker.sendMessage(): Error", inError);
            inReject(inError);
          } else {
            console.log("SMTP.Worker.sendMessage(): Ok", inInfo);
            inResolve("ok");
          }
        }
      );
    });
 // The nodemailer module does not support native async/await but uses a callback approach. To use it within async/await code, all nodemailer calls are wrapped in Promise objects. sendMessage() method internally creates an SMTP connection and then sends the email. Using Promise with <string> ensures the eventual return data type.
  } /* End sendMessage(). */


} /* End class. */
