import Link from 'next/link'

export function Header() {
  return (
    <header className="bg-white border-b border-gray-200">
      <nav className="container mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between h-16">
          <div className="flex">
            {/* Logo */}
            <div className="flex-shrink-0 flex items-center">
              <Link href="/" className="text-2xl font-bold text-primary-600">
                iMathLab
              </Link>
            </div>

            {/* Navigation Links */}
            <div className="hidden sm:ml-6 sm:flex sm:space-x-8">
              <Link
                href="/knowledge"
                className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900"
              >
                知识点
              </Link>
              <Link
                href="/exercise"
                className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900"
              >
                练习
              </Link>
              <Link
                href="/mistakes"
                className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-900"
              >
                错题本
              </Link>
            </div>
          </div>

          {/* Right side - User menu */}
          <div className="flex items-center">
            <button className="bg-primary-600 text-white px-4 py-2 rounded-md text-sm font-medium hover:bg-primary-700">
              登录
            </button>
          </div>
        </div>
      </nav>
    </header>
  )
}
