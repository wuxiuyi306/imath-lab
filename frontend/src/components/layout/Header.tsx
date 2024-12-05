import Link from 'next/link'

export function Header() {
  return (
    <header className="bg-white border-b border-gray-200">
      <nav className="container mx-auto px-4">
        <div className="flex justify-between h-16">
          <div className="flex">
            {/* Logo */}
            <div className="flex-shrink-0 flex items-center">
              <Link href="/" className="text-2xl font-bold text-primary-600">
                iMathLab
              </Link>
            </div>

            {/* Navigation Links */}
            <div className="ml-6 flex space-x-8">
              <Link
                href="/knowledge"
                className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900"
              >
                知识点
              </Link>
            </div>
          </div>
        </div>
      </nav>
    </header>
  )
}
