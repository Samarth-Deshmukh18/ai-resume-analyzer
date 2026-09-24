"use client";

import { useState } from "react";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  return (
    <main className="min-h-screen flex items-center justify-center bg-zinc-100">
      <div className="w-full max-w-sm rounded-xl bg-white p-6 shadow-lg">
        <h1 className="mb-6 text-2xl font-bold text-black">Login</h1>

        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="mb-3 w-full rounded-lg border border-zinc-300 p-3 text-black placeholder:text-zinc-400 outline-none focus:border-black"
        />

        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          className="mb-4 w-full rounded-lg border border-zinc-300 p-3 text-black placeholder:text-zinc-400 outline-none focus:border-black"
        />

        <button
          onClick={() => alert(`Email: ${email}`)}
          className="w-full rounded-lg bg-black p-3 text-white hover:bg-zinc-800"
        >
          Log in
        </button>
      </div>
    </main>
  );
}