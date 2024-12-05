export function Footer() {
  return (
    <footer className="bg-gray-50">
      <div className="container mx-auto px-4 py-4">
        <p className="text-sm text-gray-400 text-center">
          &copy; {new Date().getFullYear()} iMathLab
        </p>
      </div>
    </footer>
  )
}