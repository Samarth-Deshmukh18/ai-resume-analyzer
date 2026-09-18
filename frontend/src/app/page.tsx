export default function Home() {
  return (
    <main className="min-h-screen bg-white text-zinc-900">
      {/* Navigation */}
      <nav className="mx-auto flex max-w-7xl items-center justify-between px-6 py-6 lg:px-8">
        <div className="flex items-center gap-2">
          <div className="flex h-9 w-9 items-center justify-center rounded-lg bg-zinc-900 text-sm font-bold text-white">
            AI
          </div>
          <span className="text-xl font-bold tracking-tight">
            Resume Analyzer
          </span>
        </div>

        <div className="hidden items-center gap-8 text-sm font-medium text-zinc-600 md:flex">
          <a href="#features" className="hover:text-zinc-900">
            Features
          </a>
          <a href="#how-it-works" className="hover:text-zinc-900">
            How it works
          </a>
          <a href="#about" className="hover:text-zinc-900">
            About
          </a>
        </div>

        <div className="flex items-center gap-3">
          <button className="hidden rounded-lg px-4 py-2 text-sm font-medium text-zinc-700 hover:bg-zinc-100 sm:block">
            Log in
          </button>
          <button className="rounded-lg bg-zinc-900 px-4 py-2 text-sm font-medium text-white hover:bg-zinc-800">
            Get started
          </button>
        </div>
      </nav>

      {/* Hero */}
      <section className="mx-auto max-w-7xl px-6 pb-24 pt-20 lg:px-8 lg:pt-28">
        <div className="mx-auto max-w-4xl text-center">
          <div className="mb-6 inline-flex items-center rounded-full border border-zinc-200 bg-zinc-50 px-4 py-2 text-sm font-medium text-zinc-600">
            AI-powered resume analysis
          </div>

          <h1 className="text-5xl font-bold tracking-tight text-zinc-950 sm:text-6xl lg:text-7xl">
            Turn your resume into your
            <span className="block text-zinc-500">
              competitive advantage.
            </span>
          </h1>

          <p className="mx-auto mt-7 max-w-2xl text-lg leading-8 text-zinc-600">
            Analyze your resume, understand your ATS readiness, identify
            weaknesses, and get actionable recommendations to improve your
            chances of getting noticed.
          </p>

          <div className="mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row">
            <button className="w-full rounded-lg bg-zinc-900 px-7 py-3.5 text-sm font-semibold text-white shadow-sm hover:bg-zinc-800 sm:w-auto">
              Analyze my resume
            </button>

            <button className="w-full rounded-lg border border-zinc-300 bg-white px-7 py-3.5 text-sm font-semibold text-zinc-700 hover:bg-zinc-50 sm:w-auto">
              See how it works
            </button>
          </div>
        </div>

        {/* Product Preview */}
        <div className="mx-auto mt-20 max-w-5xl">
          <div className="overflow-hidden rounded-2xl border border-zinc-200 bg-zinc-50 shadow-2xl">
            <div className="flex items-center gap-2 border-b border-zinc-200 bg-white px-5 py-4">
              <div className="h-3 w-3 rounded-full bg-zinc-300" />
              <div className="h-3 w-3 rounded-full bg-zinc-300" />
              <div className="h-3 w-3 rounded-full bg-zinc-300" />
              <div className="ml-4 h-7 flex-1 rounded-md bg-zinc-100" />
            </div>

            <div className="grid gap-6 p-6 md:grid-cols-3">
              <div className="rounded-xl border border-zinc-200 bg-white p-6 md:col-span-1">
                <p className="text-sm font-medium text-zinc-500">
                  Resume Score
                </p>

                <div className="mt-5 flex items-end gap-2">
                  <span className="text-5xl font-bold text-zinc-900">82</span>
                  <span className="mb-2 text-sm text-zinc-500">/ 100</span>
                </div>

                <div className="mt-5 h-2 overflow-hidden rounded-full bg-zinc-100">
                  <div className="h-full w-[82%] rounded-full bg-zinc-900" />
                </div>

                <p className="mt-4 text-sm text-zinc-500">
                  Strong resume with room for improvement.
                </p>
              </div>

              <div className="rounded-xl border border-zinc-200 bg-white p-6 md:col-span-2">
                <p className="text-sm font-medium text-zinc-500">
                  AI Recommendations
                </p>

                <div className="mt-5 space-y-4">
                  <div className="rounded-lg bg-zinc-50 p-4">
                    <p className="font-medium text-zinc-900">
                      Improve your experience section
                    </p>
                    <p className="mt-1 text-sm text-zinc-500">
                      Add measurable results and outcomes to your recent roles.
                    </p>
                  </div>

                  <div className="rounded-lg bg-zinc-50 p-4">
                    <p className="font-medium text-zinc-900">
                      Strengthen keyword alignment
                    </p>
                    <p className="mt-1 text-sm text-zinc-500">
                      Several relevant skills could be highlighted more clearly.
                    </p>
                  </div>

                  <div className="rounded-lg bg-zinc-50 p-4">
                    <p className="font-medium text-zinc-900">
                      Make your achievements measurable
                    </p>
                    <p className="mt-1 text-sm text-zinc-500">
                      Use numbers, percentages, and concrete outcomes where
                      possible.
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features */}
      <section id="features" className="border-t border-zinc-200 bg-zinc-50">
        <div className="mx-auto max-w-7xl px-6 py-24 lg:px-8">
          <div className="max-w-2xl">
            <p className="text-sm font-semibold uppercase tracking-wider text-zinc-500">
              Built for job seekers
            </p>

            <h2 className="mt-3 text-3xl font-bold tracking-tight sm:text-4xl">
              Everything you need to improve your resume.
            </h2>

            <p className="mt-4 text-lg leading-8 text-zinc-600">
              Go beyond a simple score. Understand what is working, what is
              missing, and what you should change.
            </p>
          </div>

          <div className="mt-12 grid gap-6 md:grid-cols-3">
            <FeatureCard
              title="ATS Analysis"
              description="Evaluate your resume against common applicant tracking system requirements."
            />

            <FeatureCard
              title="AI Insights"
              description="Get clear strengths, weaknesses, and actionable improvement recommendations."
            />

            <FeatureCard
              title="Job Matching"
              description="Compare your resume against a job description and identify missing keywords and skills."
            />
          </div>
        </div>
      </section>

      {/* How it works */}
      <section id="how-it-works" className="bg-white">
        <div className="mx-auto max-w-7xl px-6 py-24 lg:px-8">
          <div className="text-center">
            <p className="text-sm font-semibold uppercase tracking-wider text-zinc-500">
              Simple process
            </p>

            <h2 className="mt-3 text-3xl font-bold tracking-tight sm:text-4xl">
              From resume to insights in three steps.
            </h2>
          </div>

          <div className="mt-14 grid gap-8 md:grid-cols-3">
            <Step number="01" title="Upload" description="Upload your PDF or DOCX resume." />
            <Step number="02" title="Analyze" description="Our system extracts and analyzes your resume." />
            <Step number="03" title="Improve" description="Get a score, insights, and practical recommendations." />
          </div>
        </div>
      </section>

      {/* CTA */}
      <section id="about" className="border-t border-zinc-200 bg-zinc-950">
        <div className="mx-auto max-w-4xl px-6 py-24 text-center lg:px-8">
          <h2 className="text-3xl font-bold tracking-tight text-white sm:text-4xl">
            Ready to improve your resume?
          </h2>

          <p className="mx-auto mt-5 max-w-2xl text-lg leading-8 text-zinc-400">
            Upload your resume and discover exactly where it can be stronger.
          </p>

          <button className="mt-8 rounded-lg bg-white px-7 py-3.5 text-sm font-semibold text-zinc-900 hover:bg-zinc-100">
            Get started
          </button>
        </div>
      </section>

      <footer className="bg-zinc-950 px-6 pb-10 text-center text-sm text-zinc-500">
        AI Resume Analyzer
      </footer>
    </main>
  );
}

function FeatureCard({
  title,
  description,
}: {
  title: string;
  description: string;
}) {
  return (
    <div className="rounded-xl border border-zinc-200 bg-white p-7">
      <div className="mb-5 flex h-10 w-10 items-center justify-center rounded-lg bg-zinc-900 text-sm font-bold text-white">
        AI
      </div>

      <h3 className="text-lg font-semibold">{title}</h3>

      <p className="mt-2 leading-7 text-zinc-600">{description}</p>
    </div>
  );
}

function Step({
  number,
  title,
  description,
}: {
  number: string;
  title: string;
  description: string;
}) {
  return (
    <div className="border-t border-zinc-200 pt-6">
      <p className="text-sm font-semibold text-zinc-400">{number}</p>
      <h3 className="mt-3 text-xl font-semibold">{title}</h3>
      <p className="mt-2 leading-7 text-zinc-600">{description}</p>
    </div>
  );
}