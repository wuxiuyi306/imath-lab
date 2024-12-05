'use client'

import Link from 'next/link'

// 模拟数据，实际应该从API获取
const mockKnowledgePoints = [
  {
    id: '1',
    title: '一元二次方程',
    category: {
      main: '代数',
      sub: '方程'
    },
    content: {
      summary: '一元二次方程是一种基本的代数方程，形如ax²+bx+c=0（其中a≠0）。它在数学中有广泛的应用，是初中代数的重要内容之一。',
    }
  },
  {
    id: '2',
    title: '勾股定理',
    category: {
      main: '几何',
      sub: '三角形'
    },
    content: {
      summary: '勾股定理是平面几何中最基本也是最重要的定理之一，它指出：直角三角形的两条直角边的平方和等于斜边的平方。',
    }
  },
  {
    id: '3',
    title: '相似三角形',
    category: {
      main: '几何',
      sub: '三角形'
    },
    content: {
      summary: '两个三角形，如果它们的三个角分别相等，那么这两个三角形就叫做相似三角形。',
    }
  },
  {
    id: '4',
    title: '因式分解',
    category: {
      main: '代数',
      sub: '多项式'
    },
    content: {
      summary: '因式分解是将一个多项式写成几个多项式乘积的形式的过程。',
    }
  }
]

export default function KnowledgePage() {
  return (
    <div className="container py-8">
      <h1 className="text-3xl font-bold text-gray-900 mb-6">知识点</h1>
      <div className="space-y-2">
        {mockKnowledgePoints.map((point) => (
          <Link 
            key={point.id} 
            href={`/knowledge/${point.id}`}
            className="block p-4 hover:bg-gray-50 rounded-lg transition-colors border-b"
          >
            <div className="flex items-center justify-between">
              <div>
                <h2 className="text-lg font-medium text-gray-900">{point.title}</h2>
                <p className="text-sm text-gray-500">{point.category.main} - {point.category.sub}</p>
              </div>
              <div className="text-gray-400">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="w-5 h-5">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M8.25 4.5l7.5 7.5-7.5 7.5" />
                </svg>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  )
}
