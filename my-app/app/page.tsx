'use client'

import { useState } from "react";
import { motion } from "framer-motion";

export default function NumberGuessingGame() {
  const [guess, setGuess] = useState("");
  const [message, setMessage] = useState("I am thinking of a number between 1 and 99...");
  const [secretNumber] = useState(Math.floor(Math.random() * 99) + 1);

  const handleGuess = () => {
    const userGuess = parseInt(guess);
    if (isNaN(userGuess)) {
      setMessage("Please enter a valid number!");
      return;
    }
    if (userGuess < secretNumber) {
      setMessage("Your guess is too low!");
    } else if (userGuess > secretNumber) {
      setMessage("Your guess is too high!");
    } else {
      setMessage(`Congrats! The number was: ${secretNumber}`);
    }
    setGuess("");
  };

  return (
    // <div className="flex flex-col items-center justify-center h-screen bg-cover bg-center"
    <div className="bg-opacity-custom flex items-center justify-center h-screen"
style={{ backgroundImage: "url('/ng3.jpg')" }}> 
      <motion.div 
        className="bg-black p-10 rounded-2xl shadow-x2 text-center max-w-md w-full"
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <h1 className="text-3xl shadow-lg font-bold mb-4 text-lime-400">Number Guessing Game</h1>
        <p className="text-gray-200 font-bold mb-4">{message}</p>
        <input
          type="number"
          value={guess}
          onChange={(e) => setGuess(e.target.value)}
          className="border p-2 rounded-lg w-full text-center"
          placeholder="Enter your guess"
        />
        <motion.button
          onClick={handleGuess}
          className="mt-4 bg-orange-600 text-white font-bold px-4 py-2 rounded-lg hover:bg-yellow-400"
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
        >
          Submit Guess
        </motion.button>
      </motion.div>
    </div>
  );
}
