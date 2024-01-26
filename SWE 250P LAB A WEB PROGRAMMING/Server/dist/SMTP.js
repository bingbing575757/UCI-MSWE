"use strict";
//// The primary purpose is to handle the logic of sending emails, and the Worker class receives and stores the SMTP server information required for sending emails.
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.Worker = void 0;
var nodemailer = __importStar(require("nodemailer"));
// The worker that will perform SMTP operations.
var Worker = /** @class */ (function () {
    /**
     * Constructor.
     */
    function Worker(inServerInfo) {
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
    Worker.prototype.sendMessage = function (inOptions) {
        console.log("SMTP.Worker.sendMessage()", inOptions);
        return new Promise(function (inResolve, inReject) {
            var transport = nodemailer.createTransport(Worker.serverInfo.smtp);
            //Calls nodemailer.createTransport() method, passing the server information to establish a connection with the SMTP server.
            transport.sendMail(
            //Calls transport.sendMail() method, passing in the detailed message information inOptions received from the client.
            inOptions, function (inError, inInfo) {
                if (inError) {
                    console.log("SMTP.Worker.sendMessage(): Error", inError);
                    inReject(inError);
                }
                else {
                    console.log("SMTP.Worker.sendMessage(): Ok", inInfo);
                    inResolve("ok");
                }
            });
        });
        // The nodemailer module does not support native async/await but uses a callback approach. To use it within async/await code, all nodemailer calls are wrapped in Promise objects. sendMessage() method internally creates an SMTP connection and then sends the email. Using Promise with <string> ensures the eventual return data type.
    }; /* End sendMessage(). */
    return Worker;
}()); /* End class. */
exports.Worker = Worker;
//# sourceMappingURL=SMTP.js.map