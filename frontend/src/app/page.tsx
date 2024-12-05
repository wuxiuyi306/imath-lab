export default function Home() {
  return (
    <div className="container py-12">
      <h1 className="text-4xl font-bold text-center mb-8">
        欢迎来到 iMathLab
      </h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {/* 知识点学习卡片 */}
        <div className="p-6 rounded-lg border border-gray-200 hover:shadow-lg transition-shadow">
          <h2 className="text-2xl font-semibold mb-4">知识点学习</h2>
          <p className="text-gray-600 mb-4">
            系统化的数学知识点讲解，配合AI助手，让学习更轻松
          </p>
          <button className="bg-primary-600 text-white px-4 py-2 rounded hover:bg-primary-700">
            开始学习
          </button>
        </div>

        {/* 智能练习卡片 */}
        <div className="p-6 rounded-lg border border-gray-200 hover:shadow-lg transition-shadow">
          <h2 className="text-2xl font-semibold mb-4">智能练习</h2>
          <p className="text-gray-600 mb-4">
            个性化练习题推荐，AI批改和解析，提升学习效率
          </p>
          <button className="bg-primary-600 text-white px-4 py-2 rounded hover:bg-primary-700">
            开始练习
          </button>
        </div>

        {/* 错题本卡片 */}
        <div className="p-6 rounded-lg border border-gray-200 hover:shadow-lg transition-shadow">
          <h2 className="text-2xl font-semibold mb-4">错题本</h2>
          <p className="text-gray-600 mb-4">
            智能记录和分析错题，帮助你找出知识盲点
          </p>
          <button className="bg-primary-600 text-white px-4 py-2 rounded hover:bg-primary-700">
            查看错题
          </button>
        </div>
      </div>
    </div>
  )
}
