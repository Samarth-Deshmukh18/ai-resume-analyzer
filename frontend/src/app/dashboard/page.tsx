export default function DashboardPage() {
  return (
    <main className="min-h-screen bg-zinc-100 p-8">
      <h1 className="text-3xl font-bold text-black">
        Welcome to Dashboard
      </h1>

      <p className="mt-2 text-black">
        Login successful 🎉
      </p>

      <div className="mt-8 rounded-xl bg-white p-6 shadow">
        <h2 className="text-xl font-semibold text-black">Resume Score</h2>
        <p className="mt-4 text-5xl font-bold">--</p>
      </div>
    </main>
  );
}